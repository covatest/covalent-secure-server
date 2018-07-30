import requests
from threading import Thread
import subprocess
import struct
import json

from file_helpers import upload_file_s3, download_data_file, model_folder_path
from app_const import *

def make_post_request(data, dest_url=MT_API_URL, endpoint="", headers=COVA_HEADER):
    return requests.post(dest_url + endpoint, data=data, headers=headers)


## Notifications helpers
def status_update_frontend(status_dict):
    return make_post_request(status_dict, endpoint="/status/status_update_mt")


def async_ping_to_frontend(status_dict):
    thr = Thread(target=status_update_frontend, args=(status_dict,))
    thr.start()

    return True


def start_docker(transaction_id, decryption_key):
    # TODO: harden security with separated folder for encrypted data
    cmd = """docker run --rm --network none \
       -v $(pwd)/model_input_output/%s:/model_input_output:rw \
       -v $(pwd)/encrypted_data:/encrypted_data:ro \
       -e DECRYPTION_KEY=%s \
       cs2-sandbox""" % (str(transaction_id), decryption_key)

    # TODO: change shell=False to harder security
    p = subprocess.Popen(cmd, shell=True)
    p.wait()


def run_model_in_docker(encrypted_data_hash, transaction_id):
    download_data_file(encrypted_data_hash)
    # get encryption key
    dec_key = recv_decryption_key(0, transaction_id)
    async_ping_frontend()
    # docker run
    # TODO: Started secure environment inside CS2
    # * Decrypted data and started training models inside offline sandboxes
    start_docker(transaction_id, decryption_key=dec_key)
    # TODO: Finished model training 
    # read logfile
    return {"success": True}


def recv_decryption_key(mt_id, transaction_id):
    # TODO: v1: make get request
    # i.e. verify smart contract in covachain and auto return key from
    # a concensus key server
    async_ping_to_frontend(STATUS_MSG["key_got_do"])
    
    return "cova_secret_key_is_the_fanciest"


def send_back_model_params(final_params):
    return make_post_request(final_params, endpoint="/final-status")


def release_smart_contract(smart_contract_id, success):
    # TODO: release smart contract
    num_tried = 0
    while num_tried < NUM_TRY_BDB:
        r = requests.get(COVA_CLAVE_URL + '/release_smart_contract/%s/%d' (smart_contract_id, success))
        data = json.loads(r.content)

        if not data["error"]:
            break
        else:
            num_tried += 1

    return num_tried < NUM_TRY_BDB

def full_computation_process(encrypted_data_hash, transaction_id, smart_contract_id):
    print("started processing running docker")
    async_ping_to_frontend(STATUS_MSG["starting_docker"])

    run_model_in_docker(encrypted_data_hash, transaction_id)

    print("ran docker docker")
    # send post with succes

    # log status of success/failure
    with open(model_folder_path(transaction_id) + 'log.json', 'r') as f:
        status = json.load(f)
        success, msg = status["success"], status["msg"]

    async_ping_to_frontend(msg)
    # check success
    # TODO: warning status codes
    final_params = {"transaction_id": transaction_id, "s3_url": "",
        "success": success, "status_code": int(success)}

    if success:
        # upload file to s3
        async_ping_to_frontend(STATUS_MSG["upload_s3"])
        param_url = upload_file_s3(transaction_id)
        final_params["s3_url"] = param_url

    print("final params")

    # send back model params url to MT after releasing
    release_success = release_smart_contract(smart_contract_id, int(success))
    send_back_model_params(final_params)
    async_ping_to_frontend(STATUS_MSG["contract_release"])
        
    print "smart contract realease: ", release_success

    return True

if __name__ == '__main__':
    start_docker(0)
    # for i in range(5):
    #     print make_post_request({
    #       "mt_id": 1,
    #       "transaction_id": 1,
    #       "status_code": 0,
    #       "status_msg": 'Test Message ' + str(i)
    #     }, endpoint="/status/status_update_mt")