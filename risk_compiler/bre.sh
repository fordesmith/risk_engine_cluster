#!/bin/bash -xe

# Shell script for compiling risk engine on centos7


# ----------------------------------------------------------------------
#              Install Dev Tools
# ----------------------------------------------------------------------

echo "Install Devtools"
yum update -y \
    && yum install -y \
        build-essential \
        python3-dev \
        python3-pip \
        libhdf5-serial-dev \
        software-properties-common \
        cmake3 \
        git \
        ninja-build \
        swig \
        epel-release \
        gcc-c++ \
        wget \
        libtool \
        gcc \
        glibc-devel

yum groupinstall 'Development Tools'

yum clean all

pip3 install ipywidgets \
        pandas \
        matplotlib \
        jupyter \
        bqplot \
        pythreejs \
        wheel \
        pyspark \
        jupyter_dashboards \
        six


jupyter_dashboards quick-setup --sys-prefix


# ----------------------------------------------------------------------
#              Install Boost 1.63 - later version didn`t work
# ----------------------------------------------------------------------

echo "Install Boost"
wget https://sourceforge.net/projects/boost/files/boost/1.63.0/boost_1_63_0.tar.gz
tar -xzf boost_1_*
cd boost_1_*
./bootstrap.sh --prefix=/opt/boost
./b2 install --prefix=/opt/boost --with=all

export BOOST=/opt/boost/
export BOOST_LIBS=/opt/boost/lib
export BOOST_LIBRARYDIR=/opt/boost/lib
export BOOST_INCLUDES=/opt/boost/includes

yum install -y doxygen
yum install -y graphviz
cd ../

# ----------------------------------------------------------------------
#              clone repos
# ----------------------------------------------------------------------


echo "Clone repo"

git clone https://github.com/fordesmith/OpenRiskEngine.git risk_engine
cd risk_engine
git submodule init
git submodule update


# ----------------------------------------------------------------------
#              Make risk engine
# ----------------------------------------------------------------------

echo "Make risk engine"

mkdir build
cd build
cmake3 -DBOOST_ROOT=$BOOST -DBOOST_BOOST_LIBRARYDIR=$BOOST_LIBS ..
make -j4
ctest3 -j4


