#!/bin/bash
#echo $1 $2
mkdir Input
mkdir Market
#gsutil -m cp gs://risk_params/$1/$2/* ./
#gsutil -m cp gs://market_params/$1/* ./
gsutil -m cp gs://risk_params/09-10-20/cpty_01/* ./Input/
gsutil -m cp gs://market_params/09-10-20/* ./Market/
/home/condor/risk_engine/build/App/ore "./Input/ore.xml"
gsutil cp ./Output/* gs://cpty_risk_outputs/09-10-20/cpty_01/

# python3 start_job.py $1 $2ls