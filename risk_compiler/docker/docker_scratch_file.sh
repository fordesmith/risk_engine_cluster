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

# then login again ...

docker login --username=fordesmi

docker build -t c8 .

# docker run --name r03 --rm -i -t -d fordesmi/risk-engine:latest bash
docker run --name r03 --rm -i -t -d c8

docker exec -d r03 bash /usr/local/run-risk-job.sh '09-10-20' 'cpty_01'

docker tag c8 fordesmi/risk-engine
docker push fordesmi/risk-engine