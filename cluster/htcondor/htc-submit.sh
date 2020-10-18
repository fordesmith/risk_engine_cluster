#!/bin/bash
echo $1 $2

export PYTHON_INCLUDE_DIR=/usr/include/python3.6m
export PYTHON_LIBRARY=/usr/lib64/libpython3.so
export BOOST_ROOT=$BOOST
export ORE=/home/forde_a_smith/risk_engine

echo "installed py packages"
python3 start_job.py $1 $2