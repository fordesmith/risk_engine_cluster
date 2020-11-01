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

docker build -t py1 .

# docker run --name r03 --rm -i -t -d fordesmi/risk-engine:latest bash
docker run --name r01 --rm -i -t -d --cpus="15" fordesmi/risk-engine

docker exec -d r01 bash /usr/local/run-risk-job.sh '09-10-20' 'cpty_04'

docker tag py1 fordesmi/risk-engine
docker push fordesmi/risk-engine

docker pull fordesmi/risk-engine

docker attach r01

--cpus="15"



FROM fordesmi/risk-engine
RUN printf ' \
\n #!/bin/bash  \
\n # Run risk project \
\n # $1 = job_date, $2 = cpty  \
\n mkdir Input \
\n mkdir Market  \
\n gsutil -m cp gs://risk-params/$1/$2/* ./Input  \
\n gsutil -m cp gs://market-params/$1/* ./Market  \
\n cp ./Input/*.py ./ \
\n python3 run.py \
\n gsutil -m cp ./Output/* gs://cpty-risk-outputs/$1/$2/  \
\n rm -r Input  \
\n rm -r Market  \
\n rm -r Output' > /usr/local/run-risk-job.sh

CMD bash