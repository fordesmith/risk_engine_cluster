# README for GCP Risk Cluster

This directory contains the helper code for compiling the risk engine and for setting up a cluster to calculate portfolio risk using a HT condor cluster.

Note: the compile, image creation and cluster set up works, however the HT Condor job doesn't yet run. 

The **risk_compiler** folder has two shell scripts for Debian9 and Centos7.

The **cluster** folder has a makefile that drives most of the commands you perform. The commands in the makefile are mostly wrappers around gcloud commands. The sample code has directories for the following:

* deploymentmanager/:  holds the Deployment Manager templates for creating and launching the HTCondor compute cluster.

* model/: holds the file that kicks off the risk job. 

* startup-scripts/:  holds additional scripts for creating the necessary system images for the compute cluster (based on Centos7).

Key steps, once the code has been compiled, a machine image has been created and you have the gcloud sdk and a service account:

1. Clone the GitHub repository that contains the sample code and change directories to the folder the repository was cloned to:

```
git clone https://github.com/fordesmith/risk_engine_cluster.git;
cd ris*/clu*
```

2. Create the custom condor images from the machine image with the compiled risk application

```
make createimages
```


These commands do the following tasks:
* Create a template VM for condor-master that uses a startup script that downloads and configures HTCondor.
* Stop the VM and create a snapshot for the image.
* Delete the template VM.

This can take upwards of 30 minutes to complete.

3. Deploy an HTCondor cluster into your project:

```
make createcluster
```


4. When the process is complete, use the makefile to log into the condor-submit host and determine how many cores are available in the cluster:

```
make submit-ssh job_list=XXX (e.g. '09-10-20') (Note this is currently broken - just SSH in using gcloud)
condor_status
```


5. Submit the job to htcondor-submit host - At any time, you can check on the status of your jobs with the condor_q command:

```
condor_submit risk-job-submit-job
condor_q
```
