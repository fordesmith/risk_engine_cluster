show:
	cat README.md

createimages: condor-master condor-compute condor-submit
	@echo "createimages - done"

condor-master condor-compute condor-submit:
	@if [ -z "$$(gcloud compute images list --quiet --filter='name~^$@' --format=text)" ]; then \
	   echo "" ;\
	   echo "- updating SDK" ;\
	   echo ""; \
	   yes | gcloud components install beta ;\
	   echo "" ;\
	   echo "- building $@" ;\
	   echo ""; \
	   gcloud beta compute instances create $@-template \
	     --project vannarho \
	     --zone us-east1-b \
	     --source-machine-image projects/vannarho/global/machineImages/c7-condor-img ;\
	   echo "" ;\
	   echo "- starting bootstrap $@" ;\
	   echo ""; \
	   gcloud beta compute instances add-metadata $@-template \
	     --zone us-east1-b \
	     --metadata-from-file startup-script=startup-scripts/$@.sh ;\
	   sleep 200 ;\
	   gcloud compute instances stop --zone=us-east1-b $@-template ;\
	   echo "" ;\
	   echo "- creating image for $@" ;\
	   echo ""; \
	   gcloud compute images create $@  \
	     --source-disk $@-template   \
	     --source-disk-zone us-east1-b \
	     --family htcondor-centos ;\
	   gcloud compute instances delete --quiet --zone=us-east1-b $@-template ;\
	else \
	   echo "$@ image already exists"; \
	fi


deleteimages:
	gcloud compute images delete --quiet condor-master
	gcloud compute images delete --quiet condor-compute
	gcloud compute images delete --quiet condor-submit


createcluster:
	@echo "creating a condor cluster using deployment manager scripts"
	gcloud deployment-manager deployments create condor-cluster --config deploymentmanager/condor-cluster.yaml
	
destroycluster:
	@echo "destroying the condor cluster"
	gcloud deployment-manager deployments delete condor-cluster

submit-ssh:
	@echo "upload credentials"
	gcloud compute scp /Users/fordesmith/Documents/prjts/gcp_creds/nonhashed/vannarho-fb3267082c74.json condor-submit:/home/fordesmith --zone=us-east1-b
	@echo "ssh to cordor-submit and change to condor user & home directory"
	gcloud compute ssh --project=vannarho --zone=us-east1-b condor-submit --command "su condor"
	gcloud compute ssh --project=vannarho --zone=us-east1-b condor-submit  --command "cd $HOME"
	@echo "clone source repo"
	gcloud compute ssh --project=vannarho --zone=us-east1-b condor-submit --command "git clone https://github.com/fordesmith/risk_engine_cluster.git source"
	gcloud compute ssh --project=vannarho --zone=us-east1-b condor-submit --command "export SUBMIT_ROOT=$(pwd)"
	@echo "copy files to pwd"
	gcloud compute ssh --project=vannarho --zone=us-east1-b condor-submit --command "cp $SUBMIT_ROOT/source/cluster/htcondor/* $SUBMIT_ROOT"
	gcloud compute ssh --project=vannarho --zone=us-east1-b condor-submit --command "cp $SUBMIT_ROOT/source/cluster/model/* $SUBMIT_ROOT"
	@echo "submit job"
	gcloud compute ssh --project=vannarho --zone=us-east1-b condor-submit --command "condor_submit risk-job-submit-job"
	timeout 10
	gcloud compute ssh --project=vannarho --zone=us-east1-b condor-submit --command "condor_q"
	gcloud compute ssh --project=vannarho --zone=us-east1-b condor-submit --command "cat err.0"


createjoblist:
	@echo "creating job list for $(job_date)"
	gsutil cp gs://pfe_job_specs/$(job_date)/job_list.txt ./htcondor/
	@echo "\n"
	@echo "done..."


setup:
	gcloud compute ssh --project=vannarho --zone=us-east1-b condor-submit --command "git clone https://github.com/fordesmith/risk_engine_cluster.git source"
	gcloud compute ssh --project=vannarho --zone=us-east1-b condor-submit --command "export SUBMIT_ROOT=$(pwd)"
	gcloud compute ssh --project=vannarho --zone=us-east1-b condor-submit --command "cp $SUBMIT_ROOT/source/cluster/htcondor/* $SUBMIT_ROOT"
	gcloud compute ssh --project=vannarho --zone=us-east1-b condor-submit --command "cp $SUBMIT_ROOT/source/cluster/model/* $SUBMIT_ROOT"
	gcloud compute ssh --project=vannarho --zone=us-east1-b condor-submit --command "sudo cp /home/forde_a_smith/vannarho-fb3267082c74.json $SUBMIT_ROOT"
	gcloud compute ssh --project=vannarho --zone=us-east1-b condor-submit




