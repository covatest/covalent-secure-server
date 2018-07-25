from flask import Flask
# from server_helpers import run_model_in_docker

application = Flask(__name__)


@application.route('/train_model_file')
def train_model_file():
    # process file and vars
    params = {}
    # run_model_in_docker(**params)
    
    return {}


@application.route('/recv_decryption_key')
def recv_decryption_key(name):
    # TODO: v1
    return "fancy_key"

if __name__ == '__main__':
    application.run()