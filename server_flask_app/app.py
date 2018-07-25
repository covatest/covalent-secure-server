from __future__ import print_function
from flask import Flask, request, jsonify
from threading import Thread

from server_helpers import save_file
from flask_cors import CORS


application = Flask(__name__)
CORS(application)

@application.route('/')
def hello():
    print("HELLO")
    return jsonify({"a": "HELLO"})


@application.route('/train_model_file', methods=['POST'])
def train_model_file():
    # process file
    data = request.form;
    transaction_id = data['transaction_id']
    encrypted_data_hash = data['encrypted_data_hash']
    file = request.files['file']

    if data is None:
        print("No valid request body, json missing!")
        return jsonify({'success': False})
        exit()
    else:
        print(file)
        save_file(file, transaction_id)
    # Thread(target=heavy_lift, args=(encrypted_data_hash, transaction_id)).start()

    return jsonify({"success": True})

@application.route('/ping_mt_for_file/<transaction_id>')
def ping_mt_for_file(transaction_id):
    return jsonify({
        "transaction_id": 31231,
        "aws_url":123,
        "success":True
    })

if __name__ == '__main__':
    application.run(host='0.0.0.0', port='8080')
