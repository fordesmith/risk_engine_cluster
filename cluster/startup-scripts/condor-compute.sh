#!/bin/bash

### pre-cursors
yum update -y && yum install -y wget curl net-tools vm python-pandas python-numpy python3-dev python3-pip rpm java-1.8.0-openjdk java-1.8.0-openjdk-devel
yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm


### Installing from the Repository
wget https://research.cs.wisc.edu/htcondor/yum/RPM-GPG-KEY-HTCondor
rpm --import RPM-GPG-KEY-HTCondor
cd /etc/yum.repos.d
wget https://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-rhel7.repo
yum install -y condor

mkdir -p /etc/condor/config.d/

cat <<EOF > condor_config.local
DISCARD_SESSION_KEYRING_ON_STARTUP=False
CONDOR_ADMIN=EMAIL
CONDOR_HOST=condor-master
DAEMON_LIST = MASTER, STARTD
ALLOW_WRITE = \$(ALLOW_WRITE), \$(CONDOR_HOST)

UID_DOMAIN = google.com
SUBMIT_ATTRS = RunAsOwner
RunAsOwner = True
STARTER_ALLOW_RUNAS_OWNER=TRUE
TRUST_UID_DOMAIN = True

NUM_SLOTS_TYPE_1
SLOT_TYPE_1 = c=100%, m=100%, v=100%, d=100%

EOF

mv condor_config.local /etc/condor/config.d/

systemctl start condor # starts HTCondor now via systemd, or do "condor_master" without systemd
systemctl enable condor # Make HTCondor start automatically via systemd when booting


