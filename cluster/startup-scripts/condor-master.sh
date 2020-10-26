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
UID_DOMAIN = google.com
SUBMIT_ATTRS = RunAsOwner
RunAsOwner = True
STARTER_ALLOW_RUNAS_OWNER=TRUE
TRUST_UID_DOMAIN = True
NUM_SLOTS = 1
NUM_SLOTS_TYPE_1 = 1
SLOT_TYPE_1 = cpus=100%
EOF

mv condor_config.local /etc/condor/config.d/

## start
systemctl enable condor
systemctl start condor

### check status
#condor_q
#condor_status


