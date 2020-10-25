#!/bin/bash -xe

# Shell script for compiling risk engine on centos7

# ----------------------------------------------------------------------
#              Install Dev Tools
# ----------------------------------------------------------------------

echo "Install Devtools"
yum update -y \
    && yum install -y \
        python3-devel \
        python3-pip \
        hdf5-devel \
        git \
        ninja-build \
        epel-release \
        gcc-c++ \
        wget \
        libtool \
        gcc \
        glibc-devel \
        doxygen \
        graphviz \
        libprotobuf-dev \
        protobuf-compiler \
        cmake3 \
        sudo \
        mlocate \
        which \
        curl \
        pcre-devel

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

cd /usr/local
echo "Install Boost"
wget https://sourceforge.net/projects/boost/files/boost/1.63.0/boost_1_63_0.tar.gz
tar -xzf boost_1_*
rm boost_1_63_0.tar.gz
export DBOOST_PYTHON_SOURCE=/usr/include/python3.6m
export PYTHON_INCLUDE_DIR=/usr/include/python3.6m
export PYTHON_LIBRARY=/usr/lib64/libpython3.so

cd boost_1_*
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

yum install -y doxygen
yum install -y graphviz
cd ../

# ----------------------------------------------------------------------
#              clone repos
# ----------------------------------------------------------------------


echo "Clone repo"

cd /usr/local
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
#              update permissions
# ----------------------------------------------------------------------

find /usr/local/risk_engine/build/App/ore -type f -exec chmod 777 {} \;
find /usr/local/risk_engine/build/App -type d -exec chmod 777 {} \;
find /usr/local/risk_engine/build -type d -exec chmod 777 {} \;
find /usr/local/risk_engine -type d -exec chmod 777 {} \;
find /usr/local -type d -exec chmod 777 {} \;
find /usr -type d -exec chmod 777 {} \;

# ----------------------------------------------------------------------
#              create shell script to run job
# ----------------------------------------------------------------------

printf '#!/bin/bash
# Run risk project
# $1 = job_date, $2 = cpty
mkdir Input
mkdir Market
gsutil -m cp gs://risk-params/$1/$2/* ./Input
gsutil -m cp gs://market-params/$1/* ./Market
/usr/local/risk_engine/build/App/ore "./Input/ore.xml"
gsutil cp ./Output/* gs://cpty-risk-outputs/$1/$2/
rm -r Input
rm -r Market
rm -r Output ' > /usr/local/run-risk-job.sh


echo "Done"