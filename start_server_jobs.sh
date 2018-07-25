#!/bin/bash
# amzn-ami-2018.03.a-amazon-ecs-optimized (ami-5253c32d)
curl -LOk  https://github.com/covalent-hq/covalent-secure-server/archive/master.tar.gz
tar  -xvf master.tar.gz
mv covalent-secure-server-master/* ./
rm -rf covalent-secure-server-master master.tar.gz
bash server_jobs.sh