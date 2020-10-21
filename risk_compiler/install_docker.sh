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

docker login --username=fordesmi

docker build -t fordesmi/risk-engine-c7 .


# docker tag 23ef89761a82 fordesmi/pfe-poc-img:firsttry
# docker push risk-engine/boost163_centos7:v1
docker commit dafd9b8edb84 boost163_centos7

docker push boost163_centos7
docker push latest


docker tag 331748446ea4 fordesmi/risk-engine-c7
docker push fordesmi/risk-engine-c7

docker run fordesmi/risk-engine-c7

docker logs d187fb45022e

docker ps -a


docker stop 7d07e46157bd
docker run -it -d fordesmi/risk-engine-c7
docker attach 9ab849946216

docker exec -d 85dcce91e677 stop

docker run -it -d fordesmi/risk-engine-c7
docker exec -d cd905c95fb74 cd /usr/local
docker exec -d cd905c95fb74 mkdir Input
docker exec -d cd905c95fb74 mkdir Market
docker exec -d cd905c95fb74 gsutil -m cp gs://risk_params/09-10-20/cpty_01/* ./Input
docker exec -d cd905c95fb74 gsutil -m cp gs://market_params/09-10-20/* ./Market
docker exec -d 9ab849946216 /usr/local/risk_engine/build/App/ore "./Input/ore.xml"
docker exec -d 9ab849946216 gsutil -m cp ./Output/* gs://cpty_risk_outputs/09-10-20/cpty_01/
gsutil cp ./Output/* gs://cpty_risk_outputs/$1/$2/

export CLOUDSDK_PYTHON= /usr/bin/python3 /usr/bin/python3.6 /usr/bin/python3.6-config /usr/bin/python3.6m /usr/bin/python3.6m-config /usr/bin/python3.6m-x86_64-config /usr/lib/python3.6 /usr/lib64/python3.6 /usr/include/python3.6m