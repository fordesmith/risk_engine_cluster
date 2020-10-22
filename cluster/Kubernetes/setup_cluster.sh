#!/bin/bash

kubectl apply -f risk-cluster-deployment.yaml

kubectl apply --cluster='cluster-1' -f test-job.yaml

