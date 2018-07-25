#!/bin/bash
# Amazon Linux AMI (HVM / 64-bit) amzn-ami-2018.03.b-amazon-ecs-optimized - ami-fbc1c684
curl -LOk  https://github.com/covalent-hq/covalent-secure-server/archive/master.tar.gz && tar  -xvf master.tar.gz && mv covalent-secure-server-master/* ./ && bash server_jobs.sh