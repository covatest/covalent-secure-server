import sys, os
sys.path.append('./covalent-secure-models')

from urllib2 import urlopen
import requests
import threading
import subprocess
import struct
# from cova_encryption_helpers import compute_sha256_hash_file



def recv_decryption_key(mt_id):
    # TODO: v1: make get request
    return "cova_secret_key_is_the_fanciest"

## Notifications helpers
def async_ping_frontend():
    # TODO
    urllib2.open("demo.covalent.ai/mt_status_update/something")
    return

def send_ping_to_frontend(kwargs):
    # TODO
    thr = threading.Thread(target=async_ping_frontend, kwargs=kwargs)
    thr.start()

    return True


def start_docker(transaction_id, decryption_key):
    # TODO: harder security with separated folder for encrypted data
    cmd = """docker run --rm --network none \
       -v $(pwd)/model_input_output/%s:/model_input_output:rw \
       -v $(pwd)/encrypted_data:/encrypted_data:ro \
       -e DECRYPTION_KEY=%s \
       cs2-sandbox""" % (str(transaction_id), decryption_key)

    subprocess.Popen(cmd)
    p.wait()
    print "HERE"

# run docker with
# readonly encrypted data vol and write only
# ADD the code folders
# writeonly model directory /compressed_model/trans_id:compressed_model:wo
# p.wait()

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

    return

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
