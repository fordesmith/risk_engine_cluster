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
	     --project risk-engine-293410 \
	     --zone us-east1-b \
	     --source-machine-image projects/risk-engine-293410/global/machineImages/risk-engine-img-251020 ;\
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

submit_job:
	@echo "copy input files and submit jobs"
	gcloud compute ssh \
		--project=risk-engine-293410 \
		--zone=us-east1-b \
		condor-submit \
		--command "cd /usr/local && \
		mkdir htc && \
		cd htc && \
		git clone https://github.com/fordesmith/risk_engine_cluster.git source && \
		cp ./source/cluster/htcondor/* ./ && \
		cp ./source/cluster/model/* ./ && \
		condor_submit risk-job-submit-job"
		@echo "submitted"

status:
		@echo "check status"
		gcloud compute ssh \
		--project=risk-engine-293410 \
		--zone=us-east1-b \
		condor-submit \
		--command "condor_q && condor_status"

createjoblist:
	@echo "creating job list for $(job_date)"
	gsutil cp gs://pfe-job-specs/$(job_date)/job_list.txt ./htcondor/
	@echo "\n"
	@echo "done..."

rerun: cleanup-submit-svr cleanup-buckets submit_job

cleanup-submit-svr:
	@echo "remove temp files on condor-submit"
	gcloud compute ssh \
		--project=risk-engine-293410 \
		--zone=us-east1-b \
		condor-submit \
		--command "sudo rm -r /usr/local/htc"
	@echo "done..."

cleanup-buckets:
	gsutil -m rm -r gs://cpty-risk-outputs/09-10-20/


sh_:
	gcloud compute scp /Users/fordesmith/Documents/prjts/gcp_creds/nonhashed/vannarho-fb3267082c74.json condor-submit:/home/fordesmith --zone=us-east1-b
	gcloud compute ssh --project=vannarho --zone=us-east1-b condor-submit




