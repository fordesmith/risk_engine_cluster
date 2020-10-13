#!/bin/bash

#
apt-get update && apt-get install -y wget curl net-tools vm python-pandas python-numpy python3-dev python3-pip
echo "deb http://research.cs.wisc.edu/htcondor/debian/stable/ jessie contrib" >> /etc/apt/sources.list
wget -qO - http://research.cs.wisc.edu/htcondor/debian/HTCondor-Release.gpg.key | apt-key add -
apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y condor=8.4.11~dfsg.1-1
if  dpkg -s condor >& /dev/null; then echo "yes"; else sleep 10; DEBIAN_FRONTEND=noninteractive apt-get install -y $CONDOR_INSTALL_OPT; fi;

yes | pip3 install ipywidgets \
        pandas \
        matplotlib \
        jupyter \
        bqplot \
        pythreejs \
        wheel \
        pyspark

mkdir -p /etc/condor/config.d/
cat <<EOF > condor_config.local
DISCARD_SESSION_KEYRING_ON_STARTUP=False
CONDOR_ADMIN=EMAIL
CONDOR_HOST=condor-master
DAEMON_LIST = MASTER, SCHEDD
ALLOW_WRITE = \$(ALLOW_WRITE), \$(CONDOR_HOST)
EOF

mv condor_config.local /etc/condor/config.d/

/etc/init.d/condor start
update-rc.d condor defaults
update-rc.d condor enable
