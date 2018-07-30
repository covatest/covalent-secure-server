import requests
from threading import Thread
import subprocess
import struct

from file_helpers import upload_file_s3, download_data_file


COVA_HEADER = {
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'secured-origin',
      'covalent-token': '*-d@}u%dy4p6A%JF?)$+DDO2DW4vO<'
    }

def make_post_request(data, dest_url="https://marketplace-api.covalent.ai/api",
        endpoint="", headers={}):
    return requests.post(dest_url + endpoint, data=data, headers=COVA_HEADER)


## Notifications helpers
def status_update_frontend(status_dict):
    return make_post_request(status_dict, endpoint="/status/status_update_mt")


def async_ping_to_frontend(status_dict):
    thr = Thread(target=async_ping_frontend, args=(status_dict,))
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
    # docker run
    # start_docker(transaction_id, decryption_key=dec_key)
    # read logfile
    return {"success": True}


def recv_decryption_key(mt_id, transaction_id):
    # TODO: v1: make get request
    # i.e. verify smart contract in covachain and auto return key from
    # a concensus key server
    return "cova_secret_key_is_the_fanciest"


def send_back_model_params(final_params):
    return make_post_request(final_params, endpoint="/final-status")


def full_computation_process(encrypted_data_hash, transaction_id):
    run_model_in_docker(encrypted_data_hash, transaction_id)
    # send post with succes

    # log status of success/failure
    # TODO: check
    success = True
    # check success
    final_params = {"transaction_id": transaction_id, "s3_url": "",
        "success": success, "status_code": 1}

    if success:
        # upload file to s3
        param_url = upload_file_s3(transaction_id)
        final_params["s3_url"] = param_url

    # send back model params url to MT
    send_back_model_params(final_params)

    # TODO: release smart contract

    return True

if __name__ == '__main__':
    # start_docker(0)
    for i in range(5):
        print make_post_request({
          "mt_id": 1,
          "transaction_id": 1,
          "status_code": 0,
          "status_msg": 'Test Message ' + str(i)
        }, endpoint="/status/status_update_mt")