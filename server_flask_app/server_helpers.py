import sys, os
sys.path.append('./covalent-secure-models')

from urllib2 import urlopen
import requests
import threading
import subprocess
import struct
from cova_encryption_helpers import compute_sha256_hash_file

### IO Helpers
def safe_directory_path(dir_path): 
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    return dir_path

def model_folder_path(transaction_id):
    dir_path = "../model_input_output/" + str(transaction_id)

    return safe_directory_path(dir_path)

def convert_and_save(file_data):

    text = struct.pack("b"*len(file_data),*file_data).decode('utf8')

    # save in a new directory
    with open(model_file_path(transaction_id), 'wb') as f:
        f.write(file_data)

def model_file_path(transaction_id):
    return model_folder_path(transaction_id) + '/cova_secure_model_main.py'

# encrypted data io helpers
def get_data_path(hash_encrypted_data):
    return  "./encrypted_data/" + hash_encrypted_data + ".enc"


def download_data_file(hash_encrypted_data):
    # download if file does not exist
    redownload = False
    try:
        if compute_sha256_hash_file(get_data_path(hash_encrypted_data)) != hash_encrypted_data:
            redownload = True
    except Exception as e:
        redownload = True

    if redownload:
        data = fetch_file_s3(data_hash)

        with open(encrypted_file_path,"wb+") as f:
            f.write(data)


def recv_decryption_key(mt_id):
    # TODO: v1: make get request
    return "cova_secret_key_is_the_fanciest"

def 

### Notifications helpers
# def async_ping_frontend():
#     # TODO
#     urllib2.open("demo.covalent.ai/mt_status_update/something")
#     return 

# def send_ping_to_frontend(kwargs):
#     # TODO
#     thr = threading.Thread(target=async_ping_frontend, kwargs=kwargs)
#     thr.start() 

#     return True

# s3 helpers
def fetch_file_s3(hash_encrypted_data):
    s3_url = S3_BUCKET_LINK + hash_encrypted_data + ".enc"

    return urlopen(s3_url).read()

def upload_file_s3(transaction_id):
    return True


def start_docker(transaction_id, decryption_key):
    # TODO: harder security with separated folder for encrypted data
    cmd = """docker run --rm --network none \
       -v $(pwd)/model_input_output:/model_input_output/%s/:rw \
       -v $(pwd)/encrypted_data:/encrypted_data:ro \
       -e DECRYPTION_KEY=%s \
       cs2-sandbox""" % (str(transaction_id), decryption_key)

    subprocess.Popen((cmd))
    p.wait()

# run docker with 
# readonly encrypted data vol and write only
# ADD the code folders
# writeonly model directory /compressed_model/trans_id:compressed_model:wo
# p.wait()

def run_model_in_docker(hash_encrypted_data, transaction_id):
    download_data_file(hash_encrypted_data)
    # get encryption key
    dec_key = recv_decryption_key(0)
    # docker run
    start_docker(transaction_id)
    # read logfile
    return {"success": True}

def send_back_model_params(transaction_id):
    # send the file to MT
    
    return 

def full_computation_process(hash_encrypted_data, transaction_id):
        # run model in docker
    run_model_in_docker(hash_encrypted_data, transaction_id)
    # send post with succes
    # log status of success/failure

    # upload file to s3
    upload_file_s3(transaction_id)

    # send back model params url to MT
    send_back_model_params(transaction_id)

    # release smart contract

    return True
