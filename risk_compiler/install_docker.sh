sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine


sudo yum install -y yum-utils

sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

sudo yum install -y docker-ce docker-ce-cli containerd.io

sudo systemctl start docker

sudo docker run hello-world

sudo usermod -aG docker fordesmith

then log out...

docker login --username=fordesmi

docker build -t fordesmi/risk-engine-c7 .
docker build -t test .


# docker tag 23ef89761a82 fordesmi/pfe-poc-img:firsttry
# docker push risk-engine/boost163_centos7:v1
docker commit dafd9b8edb84 boost163_centos7

docker push boost163_centos7
docker push latest


docker tag 47715e3c5d5c fordesmi/risk-engine-c7
docker push fordesmi/risk-engine-c7

docker run -d fordesmi/risk-engine-c7

docker logs d187fb45022e

docker run -it -d fordesmi/risk-engine-c7


docker stop 7d07e46157bd
docker run -it -d fordesmi/risk-engine-c7
docker attach r02

docker exec -d 85dcce91e677 stop

docker run -it -d fordesmi/risk-engine-c7
docker exec -d cd905c95fb74 cd /usr/local

docker run --name r01 --rm -i -t fordesmi/risk-engine-v1:latest bash
docker run --name r02 --rm -i -t -d fordesmi/risk-engine-v1:latest bash

docker exec -d r02 bash /usr/local/run-risk-job.sh '09-10-20' 'cpty_01'

docker exec -d r02 mkdir Input
docker exec -d r02 mkdir Market
docker exec -d r02 gsutil -m cp gs://risk_params/09-10-20/cpty_01/* ./Input
docker exec -d r02 gsutil -m cp gs://market_params/09-10-20/* ./Market
docker exec -d r02 /usr/local/risk_engine/build/App/ore "./Input/ore.xml"
docker exec -d r02 gsutil -m cp ./Output/* gs://cpty_risk_outputs/09-10-20/cpty_01/
