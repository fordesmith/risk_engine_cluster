# FROM centos:8

# MAINTAINER vannarho
# LABEL Description="Compile risk engine on centos 8 using boost"


# ----------------------------------------------------------------------
#              Install Dev Tools
# ----------------------------------------------------------------------

echo "Install Devtools" \
yum update -y \
&& yum install -y \
        python3-devel \
        python3-pip \
        git \
        epel-release \
        gcc-c++ \
        libzip-devel \
        autoconf \
        libtool \
        wget \
        libtool \
        gcc \
        glibc-devel \
        graphviz \
        cmake3 \
        sudo \
        which \
        curl \
        yum-utils

dnf config-manager --set-enabled PowerTools \
&& dnf -y install doxygen doxygen-latex doxygen-doxywizard

yum groupinstall -y 'Development Tools' \
&& yum clean all \
&& cd /usr/local

# ----------------------------------------------------------------------
#              Install gcloud sdk
# ----------------------------------------------------------------------

# Downloading gcloud package
wget https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz

# Installing the package
mkdir -p gcloud \
&& tar -C ./gcloud -xvf /tmp/google-cloud-sdk.tar.gz \
&& /usr/local/gcloud/google-cloud-sdk/install.sh

# Adding the package path to local
ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

# ----------------------------------------------------------------------
#              Install Boost latest
# ----------------------------------------------------------------------

export boost_version=1.72.0 \
&& export boost_dir=boost_1_72_0 \
&& export boost_variant=release

cd /usr/local \
&& echo "Install Boost" \
&& wget http://downloads.sourceforge.net/project/boost/boost/$boost_version/$boost_dir.tar.gz \
&& tar xfz $boost_dir.tar.gz \
&& rm $boost_dir.tar.gz \
&& export WITHPYTHON=/usr/bin/python3.6m \
&& export PYTHON_INCLUDE_DIR=/usr/include/python3.6m \
&& export PYTHON_LIBRARY=/usr/lib64/libpython3.so \
&& export PYTHONROOT=/usr/lib/python3.6 \
&& export PYTHONVER=3.6 \
&& export PYTHONLIB=/usr/lib \
&& cd ${boost_dir} \
&& echo "using python : 3.6 : /usr/bin/python3 : /usr/include/python3.6m : /usr/lib ;" >> $HOME/user-config.jam \
&& ./bootstrap.sh --prefix=/opt/boost  \
&& ./b2 install --prefix=/opt/boost --with=all \
&& cd /usr/local \
&& rm -r ${boost_dir}


# ----------------------------------------------------------------------
#              install risk engine
# ----------------------------------------------------------------------
cd /usr/local
git clone https://github.com/fordesmith/OpenRiskEngine.git risk_engine \
&& cd risk_engine \
&& git submodule init \
&& git submodule update \
&& mkdir build \
&& cd build \
&& cmake3 -DBOOST_ROOT=/opt/boost/ -DBOOST_BOOST_LIBRARYDIR=/opt/boost/lib .. \
&& make -j16 \
&& ctest3 -j17 \
&& find /usr/local/risk_engine -mindepth 1 ! -regex '^/usr/local/risk_engine/build\(/.*\)?' -delete

# ----------------------------------------------------------------------
#              update permissions
# ----------------------------------------------------------------------

find /usr/local/risk_engine/build/App/ore -type f -exec chmod 777 {} \; \
&& find /usr/local/risk_engine/build/App -type d -exec chmod 777 {} \; \
&& find /usr/local/risk_engine/build -type d -exec chmod 777 {} \; \
&& find /usr/local/risk_engine -type d -exec chmod 777 {} \; \
&& find /usr/local -type d -exec chmod 777 {} \; \
&& find /usr -type d -exec chmod 777 {} \;

# ----------------------------------------------------------------------
#              create shell script to run job
# ----------------------------------------------------------------------

printf ' \
\n #!/bin/bash  \
\n # Run risk project \
\n # $1 = job_date, $2 = cpty  \
\n mkdir Input \
\n mkdir Market  \
\n gsutil -m cp gs://risk-params/$1/$2/* ./Input  \
\n gsutil -m cp gs://market-params/$1/* ./Market  \
\n /usr/local/risk_engine/build/App/ore "./Input/ore.xml"  \
\n gsutil -m cp ./Output/* gs://cpty-risk-outputs/$1/$2/  \
\n rm -r Input  \
\n rm -r Market  \
\n rm -r Output' > /usr/local/run-risk-job.sh

