#!/bin/bash
# Amazon Linux AMI (HVM / 64-bit)
curl -LOk  https://github.com/covalent-hq/covalent-secure-server/archive/master.tar.gz
tar  -xvf master.tar.gz
mv covalent-secure-server-master/* ./
rm -rf covalent-secure-server-master master.tar.gz
bash server_jobs.sh