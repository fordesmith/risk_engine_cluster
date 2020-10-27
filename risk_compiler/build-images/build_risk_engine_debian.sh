#!/bin/bash -xe

# ----------------------------------------------------------------------
#              Install Dev Tools
# ----------------------------------------------------------------------

echo "Install Devtools"
apt-get update \
    && apt-get install -y \
        build-essential \
        python3-dev \
        python3-pip \
        libhdf5-serial-dev \
        software-properties-common \
        cmake3 \
        git \
        ninja-build \
        swig \

    && apt-get clean

pip3 install ipywidgets \
        pandas \
        matplotlib \
        jupyter \
        bqplot \
        pythreejs \
        wheel \
        pyspark \
        jupyter_dashboards


jupyter_dashboards quick-setup --sys-prefix

# ----------------------------------------------------------------------
#              clone repos
# ----------------------------------------------------------------------


echo "Clone repos"

git clone https://github.com/fordesmith/OpenRiskEngine.git risk_engine
git clone https://github.com/fordesmith/ORE-SWIG.git risk_swig

git clone https://github.com/opensourcerisk/ore-swig risk_swig

cd risk_engine
git submodule init
git submodule update


# ----------------------------------------------------------------------
#              Install Boost
# ----------------------------------------------------------------------

echo "Install Boost"
# as super user
wget https://dl.bintray.com/boostorg/release/1.74.0/source/boost_1_74_0.tar.gz
tar -xzf boost_1_*
cd boost_1_*
./bootstrap.sh --prefix=/opt/boost
./b2 install --prefix=/opt/boost --with=all

export BOOST=/opt/boost/

apt-get install -y doxygen
apt-get install -y graphviz


# ----------------------------------------------------------------------
#              Make risk engine
# ----------------------------------------------------------------------

echo "Make risk engine"
export DBOOST_ROOT=$BOOST
export DBOOST_LIBRARYDIR=$BOOST
mkdir build
cd build
cmake3 ..
make -j17
ctest -j17

# Shell script for compiling risk engine on debian9

# ----------------------------------------------------------------------
passwd -d
# ----------------------------------------------------------------------

cd ../../
git clone https://github.com/fordesmith/ORE-SWIG.git risk_swig
cd risk_swig
git submodule init
git submodule update
mkdir build
cd build

export PYTHON_INCLUDE DIR=/usr/include/python3.7
export PYTHON_LIBRARY=/usr/lib/python3.7
export BOOST_LIBRARYDIR=$BOOST
export BOOST_ROOT=$BOOST
export ORE=/home/forde_a_smith/risk_engine

set LANG and LC ALL to en US.UTF-8
set LC NUMERIC to C.


cmake -G Ninja ..

ninja

export PYTHONPATH=/home/forde_a_smith/risk_swig/build/OREAnalytics-SWIG/Python

export PYTHONPATH=/home/forde_a_smith/risk_swig/build/OREAnalytics-SWIG/Python
cd ../
cd /OREAnalytics/Python/Examples
python3 ore.py


