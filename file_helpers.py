import boto3
import random
from urllib2 import urlopen
from cova_encryption_helpers import compute_sha256_hash_file

S3_ACCESS_KEY = "AKIAJR7A5QTYBLQMBOLA"
S3_SECRET_KEY = "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"


# s3 helpers
def fetch_file_s3(encrypted_data_hash):
    s3_url = S3_BUCKET_LINK + encrypted_data_hash + ".enc"

    return urlopen(s3_url).read()


def generate_rand_filename_s3(transaction_id):
    rand_seed = hex(random.getrandbits(32))
    
    path = 'model-param-dumps/model_params_%s_%s.pkl' % (rand_seed, str(transaction_id))

    return path


def final_s3_url(path):
    return 'https://s3.amazonaws.com/data-marketplace-storage/' + path


def upload_file_s3(transaction_id):
    s3 = boto3.client(
        's3',
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_KEY
    )

    bucket_name = 'data-marketplace-storage'
    source_file_path = model_params_file_path(transaction_id)
    path = generate_rand_filename_s3(transaction_id)
    s3.upload_file(model_params_file_path, bucket_name, path)

    return final_s3_url(path)


### IO Helpers
def safe_directory_path(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    return dir_path


def model_folder_path(transaction_id):
    dir_path = "model_input_output/" + str(transaction_id)

    return safe_directory_path(dir_path)


def save_file(file, transaction_id):
    # save in a new directory
    file.save(model_file_path(transaction_id))


def model_file_path(transaction_id):
    return model_folder_path(transaction_id) + '/cova_secure_model_main.py'


def model_params_file_path(transaction_id):
    return model_folder_path(transaction_id) + '/model_params.pkl'


# encrypted data io helpers
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
    else:
        print "File locally exists"

if __name__ == '__main__':
    upload_file_s3(13213)
    