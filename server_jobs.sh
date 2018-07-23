#!/bin/bash
# install python pip 
# install packages: pynacl
# wget data
# decrypt file and save
# wget the secure library
# start a docker core
# send key to DO
# send encrypted data to MT

echo "start"
docker run --rm \
	--network none \
	--read-only --tmpfs /tmp \
	--name no-net-cova-core \
	test-cs2 >> output.txt
# cat output.txt
echo "end"