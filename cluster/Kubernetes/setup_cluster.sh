#!/bin/bash

gcloud container clusters create risk-cluster

gcloud container clusters get-credentials risk-cluster

kubectl create deployment risk-server --image=fordesmi/risk-engine-v1

kubectl apply -f risk-cluster-deployment.yaml

kubectl apply -f t1.yaml