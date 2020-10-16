#!/bin/bash -xe

# Shell script for compiling risk engine on centos7or8


# ----------------------------------------------------------------------
#              Install Dev Tools
# ----------------------------------------------------------------------

echo "Install Devtools"
yum update -y \
    && yum install -y \
        python3-devel \
        python3-pip \
        hdf5-devel \
        cmake3 \
        git \
        ninja-build \
        swig \
        epel-release \
        gcc-c++ \
        wget \
        libtool \
        glibc-devel \
        doxygen \
        graphviz

yum groupinstall -y 'Development Tools'

yum clean all

yes | pip3 install ipywidgets \
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
make -j17
ctest3 -j17



# ----------------------------------------------------------------------
#              Make swig - TO DO - FIX
# ----------------------------------------------------------------------

cd ../../
git clone https://github.com/fordesmith/ORE-SWIG.git risk_swig
cd risk_swig
git submodule init
git submodule update
mkdir build
cd build

export PYTHON_INCLUDE_DIR=/usr/include/python3.6m
export PYTHON_LIBRARY=/usr/lib64/libpython3.so
export BOOST_ROOT=$BOOST
export ORE=/home/forde_a_smith/risk_engine

set LANG and LC ALL to en US.UTF-8
set LC NUMERIC to C.

# cmake3 -G Ninja ..

cmake3 -G Ninja \
-D ORE=$ORE \
-D BOOST_ROOT=$BOOST \
-D BOOST_LIBRARYDIR=$BOOST_LIBRARYDIR \
-D PYTHON_LIBRARY=$PYTHON_LIBRARY \
-D PYTHON_INCLUDE_DIR=$PYTHON_INCLUDE_DIR \
..

cmake3 \
-D ORE=$ORE \
-D BOOST_ROOT=$BOOST \
-D BOOST_LIBRARYDIR=$BOOST_LIBRARYDIR \
-D PYTHON_LIBRARY=$PYTHON_LIBRARY \
-D PYTHON_INCLUDE_DIR=$PYTHON_INCLUDE_DIR \
..

cmake -j17

ninja

export PYTHONPATH=/home/forde_a_smith/risk_swig/build/OREAnalytics-SWIG/Python
cd ../
cd /OREAnalytics/Python/Examples
python3 ore.py


