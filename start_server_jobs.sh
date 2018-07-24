#!/bin/bash
wget  https://github.com/covalent-hq/covalent-secure-server/archive/master.tar.gz
tar  -xvf master.tar.gz
rm master.tar.gz
mv covalent-secure-servrer-master/* ./
rm -rf covalent-secure-server-master
bash server_jobs.sh