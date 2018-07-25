import sys, os
sys.path.append('./covalent-secure-models')

import requests
from threading import Thread
import subprocess
import struct
# from cova_encryption_helpers import compute_sha256_hash_file
from file_helpers import upload_file_s3


COVA_HEADER = {
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'secured-origin',
      'covalent-token': '*-d@}u%dy4p6A%JF?)$+DDO2DW4vO<'
    }

def make_post_request(data, dest_url="https://marketplace.covalent.ai/api",
        endpoint="", headers={}):
    return requests.post(dest_url + endpoint, data=data, headers=COVA_HEADER)


def recv_decryption_key(mt_id):
    # TODO: v1: make get request
    return "cova_secret_key_is_the_fanciest"


## Notifications helpers
def status_update_frontend(status_dict):
    return make_post_request(status_dict, endpoint="/status/status_update_mt")


def async_ping_to_frontend(status_dict):
    thr = Thread(target=async_ping_frontend, args=(status_dict,))
    thr.start()

    return True


def start_docker(transaction_id, 
    decryption_key="cova_secret_key_is_the_fanciest"):
    # TODO: harden security with separated folder for encrypted data
    cmd = """docker run --rm --network none \
       -v $(pwd)/model_input_output/%s:/model_input_output:rw \
       -v $(pwd)/encrypted_data:/encrypted_data:ro \
       -e DECRYPTION_KEY=%s \
       cs2-sandbox""" % (str(transaction_id), decryption_key)

    p = subprocess.Popen(cmd, shell=True)
    p.wait()


def run_model_in_docker(encrypted_data_hash, transaction_id):
    download_data_file(encrypted_data_hash)
    # get encryption key
    dec_key = recv_decryption_key(0)
    # docker run
    start_docker(transaction_id)
    # read logfile
    return {"success": True}


def send_back_model_params(transaction_id):
    # send the file to MT
    url = upload_file_s3(transaction_id)

    requests
    return url

def full_computation_process(encrypted_data_hash, transaction_id):
        # run model in docker
    run_model_in_docker(encrypted_data_hash, transaction_id)
    # send post with succes
    # log status of success/failure

    # upload file to s3
    upload_file_s3(transaction_id)

    # send back model params url to MT
    send_back_model_params(transaction_id)

    # release smart contract

    return True

if __name__ == '__main__':
    start_docker(0)