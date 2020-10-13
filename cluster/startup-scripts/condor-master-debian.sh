#!/bin/bash



apt-get update
echo Y | apt-get install apt-transport-https
apt-get install -y wget curl net-tools vm
echo "deb http://research.cs.wisc.edu/htcondor/debian/stable/ jessie contrib" >> /etc/apt/sources.list
wget -qO - http://research.cs.wisc.edu/htcondor/debian/HTCondor-Release.gpg.key | apt-key add -
apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y condor=8.4.11~dfsg.1-1
if  dpkg -s condor >& /dev/null; then echo "yes"; else sleep 10; DEBIAN_FRONTEND=noninteractive apt-get install -y condor=8.4.11~dfsg.1-1; fi;

mkdir -p /etc/condor/config.d/

cat <<EOF > condor_config.local
DISCARD_SESSION_KEYRING_ON_STARTUP=False
DAEMON_LIST = MASTER, COLLECTOR, NEGOTIATOR, SCHEDD, STARTD
CONDOR_ADMIN=EMAIL
ALLOW_WRITE = \$(ALLOW_WRITE),10.240.0.0/16
CONDOR_HOST=condor-master
EOF

mv condor_config.local /etc/condor/config.d/

/etc/init.d/condor start
update-rc.d condor defaults
update-rc.d condor enable
