#!/bin/bash
# install python pip 
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python get-pip.py --user
# rm get-pip.py
# pip install gunicorn flask --user # do version

# wget the secure library
# wget  https://github.com/covalent-hq/covalent-secure-server/archive/master.tar.gz
# tar  -xvf master.tar.gz
# rm master.tar.gz

# build the inner docker core

# start the python server
# cd server_flask_app
# gunicorn -w 3 -b 0.0.0.0:8000 wsgi

echo "start"
docker run --rm \
	--network none \
	--read-only --tmpfs /tmp \
	--name no-net-cova-core \
	test-cs2 >> output.txt
# cat output.txt
echo "end"