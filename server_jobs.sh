#!/bin/bash
rm -rf covalent-secure-server-master master.tar.gz
install python pip 
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py --user
rm get-pip.py
pip install gunicorn==19.9.0 flask==1.0.2 Flask-Cors==3.0.6 boto3==1.4.1 --user # do version

# curl the secure library
curl -LOk  https://github.com/covalent-hq/covalent-secure-models/archive/master.tar.gz
tar  -xvf master.tar.gz

# build the inner docker core
docker build -t cs2-sandbox .

# start the python server
cd server_flask_app
gunicorn -w 3 -b 0.0.0.0:8080 wsgi