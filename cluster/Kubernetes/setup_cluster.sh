#!/bin/bash

gcloud container clusters create risk-engine --num-nodes=3

kubectl create deployment risk-engine --image=gcr.io/google-samples/hello-app:1.0




