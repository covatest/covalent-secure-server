from flask import Flask, request, jsonify
from threading import Thread

# from server_helpers import run_model_in_docker

application = Flask(__name__)

@application.route('/train_model_file/<transaction_id>/<hash_encrypted_data>')
def train_model_file(transaction_id, hash_encrypted_data):
    # process file
    data = request.get_json()
    if data is None:
        print("No valid request body, json missing!")
        
        return jsonify({'success': False})
        exit()
    else:
        file_data = data['file']['data']['data']
        convert_and_save(file_data)

    # Thread(target=heavy_lift, args=(hash_encrypted_data, transaction_id)).start()

    return jsonify({"success": True})

@application.route('/ping_mt_for_file/<transaction_id>')
def ping_mt_for_file(transaction_id):
    requests.post()
    {   
        "transaction_id":
        "aws_url":
        "success":
    }
    return

if __name__ == '__main__':
    application.run()