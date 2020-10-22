
#!/bin/bash
# Run risk project
# $1 = job_date, $2 = cpty
mkdir Input
mkdir Market
gsutil -m cp gs://risk_params/$1/$2/* ./Input
gsutil -m cp gs://market_params/$1/* ./Market
/usr/local/risk_engine/build/App/ore "./Input/ore.xml"
gsutil cp ./Output/* gs://cpty_risk_outputs/$1/$2/
rm Input
rm Market
rm Output 