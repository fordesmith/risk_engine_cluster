#!/bin/bash

gcloud container clusters create risk-cluster

gcloud beta container --project "risk-engine-293410" clusters create "cluster-re" --region "us-central1-a" --no-enable-basic-auth --cluster-version "1.16.13-gke.401" --machine-type "e2-highmem-4" --image-type "COS" --disk-type "pd-standard" --disk-size "250" --metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --num-nodes "2" --enable-stackdriver-kubernetes --enable-ip-alias --network "projects/risk-engine-293410/global/networks/default" --subnetwork "projects/risk-engine-293410/regions/australia-southeast1/subnetworks/default" --default-max-pods-per-node "110" --no-enable-master-authorized-networks --addons HorizontalPodAutoscaling,HttpLoadBalancing --enable-autoupgrade --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade 0


gcloud container clusters get-credentials risk-cluster

kubectl create deployment risk-server --image=fordesmi/risk-engine

kubectl apply -f risk-cluster-deployment.yaml

kubectl apply -f t1.yaml

/usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/bin/kubectl create deployment risk-server --image=fordesmi/risk-engine


gcloud container clusters create risk-cluster --project "risk-engine-293410" --region "australia-southeast1" --no-enable-basic-auth --cluster-version "1.16.13-gke.401" --machine-type "e2-highmem-4" --image-type "COS" --disk-type "pd-standard" --disk-size "200" --metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --num-nodes "2" --enable-stackdriver-kubernetes --enable-ip-alias --network "projects/risk-engine-293410/global/networks/default" --subnetwork "projects/risk-engine-293410/regions/australia-southeast1/subnetworks/default" --default-max-pods-per-node "110" --no-enable-master-authorized-networks --addons HorizontalPodAutoscaling,HttpLoadBalancing --enable-autoupgrade --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade
/usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/bin/kubectl logs risk-engine-5b6cb4fb9d-9sxr5
