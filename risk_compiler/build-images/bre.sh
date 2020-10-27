#!/bin/bash -xe

# Shell script for compiling risk engine on centos7or8


export _ME_=$(whoami)

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
        gcc \
        glibc-devel \
        doxygen \
        graphviz


yum groupinstall -y 'Development Tools'

yum clean all


# ----------------------------------------------------------------------
#              Install Boost 1.63 - later version didn`t work
# ----------------------------------------------------------------------

echo "Install Boost"


wget https://sourceforge.net/projects/boost/files/boost/1.63.0/boost_1_63_0.tar.gz
tar -xzf boost_1_*
rm boost_1_63_0.tar.gz

export WITHPYTHON=/usr/bin/python3.6m
export PYTHON_INCLUDE_DIR=/usr/include/python3.6m
export PYTHON_LIBRARY=/usr/lib64/libpython3.so
export PYTHONROOT=/usr/lib64/python3.6
export PYTHONVER=3.6
export PYTHONLIB=/usr/lib64/

cd boost_1_63_0
cat <<EOF > user-config.jam
using python : 3.6 : /usr/bin/python3 : /usr/include/python3.6m : /usr/lib ;
EOF
cp ./user-config.jam $HOME/user-config.jam
./bootstrap.sh --prefix=/opt/boost
./b2 install --prefix=/opt/boost --with=all



export BOOST=/opt/boost/
export BOOST_LIBS=/opt/boost/lib
export BOOST_LIBRARYDIR=/opt/boost/lib
export BOOST_INCLUDES=/opt/boost/includes

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

find /home -type d -exec chmod 777 {} \;
find /home/$_ME_ -type d -exec chmod 777 {} \;
find /home/$_ME_ /risk_engine -type d -exec chmod 777 {} \;
find /home/$_ME_ /risk_engine/App -type d -exec chmod 777 {} \;
find /home/$_ME_ /risk_engine/build -type d -exec chmod 777 {} \;
find /home/$_ME_ /risk_engine/build/App -type d -exec chmod 777 {} \;
find /home/$_ME_ /risk_engine/build/App/ore -type f -exec chmod 777 {} \;
