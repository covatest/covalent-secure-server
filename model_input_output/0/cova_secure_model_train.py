# example MT code
def process_data_fn(df):
    return df.head(500)

MODEL = {
    "model_name": "svc",    {
  "S3_BUCKET_LINK": "https://s3.amazonaws.com/data-marketplace-storage",
  "S3_ACCESS_KEY": "",
  "S3_SECRET_KEY": ""
}
    "model_params": {} ,
    "X_feats" : ["mean radius",
        "mean texture",
        "mean perimeter",
        "mean area",
        "mean smoothness",
        "mean compactness",
        "mean concavity",
        "mean concave points",
        "mean symmetry",
        "mean fractal dimension"],
    "Y_feats":["malignant"],
    "data_hash":data_hash
    }


