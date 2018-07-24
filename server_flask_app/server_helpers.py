import sys
sys.path.append('./covalent-secure-models')

from urllib2 import urlopen
from cova_encryption_helpers import compute_sha256_hash_file


def fetch_file_s3(encrypted_data_hash):
    s3_url = S3_BUCKET_LINK + encrypted_data_hash + ".enc"

    return urlopen(s3_url).read()


def get_data_path(encrypted_data_hash):
    return  "./encrypted_data/" + encrypted_data_hash + ".enc"


def download_data_file(encrypted_data_hash):
    # download if file does not exist
    redownload = False
    try:
        if compute_sha256_hash_file(get_data_path(encrypted_data_hash)) != encrypted_data_hash:
            redownload = True
    except Exception as e:
        redownload = True

    if redownload:
        data = fetch_file_s3(data_hash)

        with open(encrypted_file_path,"wb+") as f:
            f.write(data)

def start_docker(trans_hash, decryption_key):
    cmd = """docker run --rm --network none --read-only \
       -v compressed_model:/compressed_models/%s:rw \
       -v encrypted_data:/encrypted_data:ro \
       -e DECRYPTION_KEY=%s \
       cs2-sandbox""" % (trans_hash, decryption_key)
    p.wait()

# run docker with 
# readonly encrypted data vol and write only
# ADD the code folders
# writeonly model directory /compressed_model/trans_hash:compressed_model:wo
# p.wait()

def run_model_in_docker():
    download_data_file(encrypted_data_hash)
    # docker run
    start_docker(trans_hash)
    # read logfile
    return {"success": True}

def send_back_model_params(model_params_filepath):
    # send the file to MT
    
    return 
