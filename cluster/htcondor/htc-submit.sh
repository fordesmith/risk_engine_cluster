#!/bin/bash
echo $1 $2

yes | pip3 install ipywidgets \
        pandas \
        matplotlib \
        bqplot \
        pythreejs \
        wheel \
        six \
        google-cloud-storage

echo "installed py packages"

python3 start_job.py $1 $2