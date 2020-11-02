#!/bin/bash

gcloud container clusters create risk-cluster

gcloud beta container --project "risk-engine-293410" clusters create "risk-cluster-clone-1" --zone "us-central1-c" --no-enable-basic-auth --cluster-version "1.16.13-gke.401" --machine-type "e2-highmem-4" --image-type "COS" --disk-type "pd-standard" --disk-size "100" --metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/cloud-platform" --max-pods-per-node "110" --num-nodes "3" --enable-stackdriver-kubernetes --enable-ip-alias --network "projects/risk-engine-293410/global/networks/default" --subnetwork "projects/risk-engine-293410/regions/us-central1/subnetworks/default" --default-max-pods-per-node "110" --no-enable-master-authorized-networks --addons HorizontalPodAutoscaling,HttpLoadBalancing --enable-autoupgrade --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade 0
gcloud container clusters get-credentials risk-cluster

kubectl apply -f deployment.yaml

kubectl apply -f test-job.yaml

