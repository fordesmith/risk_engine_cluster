
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
	     --source-machine-image projects/vannarho/global/machineImages/centos7-risk-engine ;\
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
	     --source-disk-zone us-east1-b
	     --family htcondor-centos ;\
	   gcloud compute instances delete --quiet --zone=us-east1-b $@-template ;\
	else \
	   echo "$@ image already exists"; \
	fi


deleteimages:
	-gcloud compute images delete --quiet condor-master
	-gcloud compute images delete --quiet condor-compute
	-gcloud compute images delete --quiet condor-submit


createcluster:
	@echo "creating a condor cluster using deployment manager scripts"
	gcloud deployment-manager deployments create condor-cluster --config deploymentmanager/condor-cluster.yaml
	
destroycluster:
	@echo "destroying the condor cluster"
	gcloud deployment-manager deployments delete condor-cluster

submit-ssh:
	@echo "before sshing to the submit host, let me copy some of the files there to make"
	@echo "it easier for you."
	@echo "  - copying the model"
	@echo "creating job list for $(job_date)"
	gsutil cp gs://pfe_job_specs/$(job_date)/job_list.txt ./htcondor/
	@echo "  - copying the datafiles"
	gcloud compute ssh condor-submit --command "gsutil cp ./model/* ."
	gcloud compute ssh condor-submit --command "gsutil cp ./htcondor/* ."
	@echo "\n"
	@echo "done..."
	@echo "now just sshing"
	gcloud compute ssh condor-submit

createjoblist:
	@echo "creating job list for $(job_date)"
	gsutil cp gs://pfe_job_specs/$(job_date)/job_list.txt ./htcondor/
	@echo "\n"
	@echo "done..."


clean:
	rm link.file WIKI_PRICES*.zip WIKI_PRICES*.csv 
