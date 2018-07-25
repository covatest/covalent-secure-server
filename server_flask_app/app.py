from flask import Flask, request, jsonify
from threading import Thread

from server_helpers import convert_and_save

application = Flask(__name__)

@application.route('/')
def hello():
    print "HELLO"
    return jsonify({"a": "HELLO"})


@application.route('/train_model_file', methods=['POST'])
def train_model_file():
    # process file
    data = request.get_json()
    print data
    transaction_id = data['transaction_id']
    hash_encrypted_data = data['hash_encrypted_data']

    if data is None:
        print("No valid request body, json missing!")
        
        return jsonify({'success': False})
        exit()
    else:
        file_data = data['file']['data']['data']
        convert_and_save(file_data, transaction_id)

    # Thread(target=heavy_lift, args=(hash_encrypted_data, transaction_id)).start()

    return jsonify({"success": True})

@application.route('/ping_mt_for_file/<transaction_id>')
def ping_mt_for_file(transaction_id):
    return jsonify({   
        "transaction_id": 31231,
        "aws_url":123,
        "success":True
    })

if __name__ == '__main__':
    application.run()