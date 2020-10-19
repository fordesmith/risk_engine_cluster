#!/bin/bash
echo $1 $2
mkdir Input
mkdir Market
gsutil -m cp gs://risk_params/$1/$2/* ./
gsutil -m cp gs://market_params/$1/* ./
/home/condor/risk_engine/build/App/ore "./Input/ore.xml"
gsutil cp ./Output/* gs://cpty_risk_outputs/$1/$2

# python3 start_job.py $1 $2