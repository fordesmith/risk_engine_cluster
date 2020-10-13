#!/bin/bash

## https://htcondor.readthedocs.io/en/latest/admin-manual/quick-start-condor-pool.html?highlight=quick%20start#quick-start-setting-up-an-htcondor-pool


### pre-cursors
yum update
yum install -y apt-transport-https wget curl net-tools vm rpm


### Installing from the Repository
wget https://research.cs.wisc.edu/htcondor/yum/RPM-GPG-KEY-HTCondor
rpm --import RPM-GPG-KEY-HTCondor
cd /etc/yum.repos.d
wget https://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-rhel7.repo
yum install -y condor

mkdir -p /etc/condor/config.d/

cat <<EOF > condor_config.local
DISCARD_SESSION_KEYRING_ON_STARTUP=False
DAEMON_LIST = MASTER, COLLECTOR, NEGOTIATOR, SCHEDD, STARTD
CONDOR_ADMIN=EMAIL
ALLOW_WRITE = \$(ALLOW_WRITE),10.240.0.0/16
CONDOR_HOST=condor-master
EOF

mv condor_config.local /etc/condor/config.d/

## start
systemctl enable condor
systemctl start condor

### check status
#condor_q
#condor_status


