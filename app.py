from __future__ import print_function
from flask import Flask, request, jsonify
from multiprocessing import Process

from file_helpers import save_file
from server_helpers import full_computation_process
from flask_cors import CORS


application = Flask(__name__)
CORS(application)

@application.route('/<test>')
def hello_test(test):
    msg = "HELLO " + test
    print(msg)
    return jsonify({"msg": msg})


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
        save_file(file, transaction_id)
    p = Process(target=full_computation_process, args=(encrypted_data_hash, transaction_id))
    p.start()

    return jsonify({"success": True})

@application.route('/ping_mt_for_file/<transaction_id>')
def ping_mt_for_file(transaction_id):
    return jsonify({
        "transaction_id": transaction_id,
        "aws_url": "",
        "success":True
    })

if __name__ == '__main__':
    # TODO: ping back to SGX once spawned
    application.run(host='0.0.0.0', port='8080')
