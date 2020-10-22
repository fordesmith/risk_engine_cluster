
sudo systemctl start docker

docker run --name r01 --rm -i -t fordesmi/risk-engine-c7 bash

docker run --name r02 --rm -i -t -d fordesmi/risk-engine-c7 bash
docker exec -d r02 mkdir Input
docker exec -d r02 mkdir Market
docker exec -d r02 gsutil -m cp gs://risk_params/09-10-20/cpty_01/* ./Input
docker exec -d r02 gsutil -m cp gs://market_params/09-10-20/* ./Market
docker exec -d r02 /usr/local/risk_engine/build/App/ore "./Input/ore.xml"
docker exec -d r02 gsutil -m cp ./Output/* gs://cpty_risk_outputs/09-10-20/cpty_01/