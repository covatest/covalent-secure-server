import json

COVA_HEADER = {
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'secured-origin',
      'covalent-token': '*-d@}u%dy4p6A%JF?)$+DDO2DW4vO<'
    }

MT_API_URL = "https://marketplace-api.covalent.ai/api"


# s3 consts
S3_BUCKET_LINK = "https://s3.amazonaws.com/data-marketplace-storage"
S3_ACCESS_KEY = ""
S3_SECRET_KEY = ""

with open("/.creds/s3_cred", "r") as f:
    s3_creds = json.load(f)
    S3_ACCESS_KEY = s3_creds["S3_ACCESS_KEY"]
    S3_SECRET_KEY = s3_creds["S3_SECRET_KEY"]

SGX_URL = "http://covachain.covalent.ai"
NUM_TRY_BDB = 5