#!/bin/bash
#echo $1 $2
sudo mkdir Input
sudo mkdir Market
#gsutil -m cp gs://risk_params/$1/$2/* ./
#gsutil -m cp gs://market_params/$1/* ./
sudo gsutil -m cp gs://risk_params/09-10-20/cpty_01/* ./Input/
sudo gsutil -m cp gs://market_params/09-10-20/* ./Market/
sudo /home/condor/risk_engine/build/App/ore "./Input/ore.xml"
sudo gsutil cp ./Output/* gs://cpty_risk_outputs/09-10-20/cpty_01/

# python3 start_job.py $1 $2ls