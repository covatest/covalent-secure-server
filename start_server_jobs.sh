#!/bin/bash
# amzn-ami-2018.03.a-amazon-ecs-optimized (ami-5253c32d)
curl -LOk  https://github.com/covalent-hq/covalent-secure-server/archive/master.tar.gz
tar  -xvf master.tar.gz
rm master.tar.gz
mv covalent-secure-servrer-master/* ./
rm -rf covalent-secure-server-master
bash server_jobs.sh