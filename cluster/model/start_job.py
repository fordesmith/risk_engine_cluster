# export GOOGLE_APPLICATION_CREDENTIALS=/Users/fordesmith/Documents/prjts/gcp_cluster/vannarho-9ce81e1e196e.json

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import sys
import os
from risk_helper import RiskEngine
from google.cloud import storage
from os import makedirs
from os.path import isdir, isfile, join
from os import listdir


def get_input_blobs(bucket_name,prefix,dl_dir,storage_client):
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=prefix)  # Get list of files
    if isdir(dl_dir) == False:
        makedirs(dl_dir)
    for blob in blobs:
        filename = blob.name.replace(prefix, dl_dir)
        print("Downloading inputs....")
        print(filename)
        if filename != dl_dir:
            blob.download_to_filename(filename)  # Download

def upload_blob(bucket_name, source_dir, destination_blob_folder,storage_client):
    bucket = storage_client.get_bucket(bucket_name)
    files_to_upload = [f for f in listdir(source_dir) if isfile(join(source_dir, f))]
    for file in files_to_upload:
        print("Uploading outputs....")
        print(source_dir + file)
        blob = bucket.blob(destination_blob_folder + file)
        blob.upload_from_filename(source_dir + file)


def main(job_date, cpty):
    conf = SparkConf().setAppName('risk_job' + '_' + job_date + '_' + cpty)
    sc = SparkContext(conf=conf)
    spark = SparkSession(sc)
    base_path = os.getcwd() + "/"
    os.makedirs("Input", mode=0o777, exist_ok=False)
    os.makedirs("Market", mode=0o777, exist_ok=False)
    os.makedirs("Output", mode=0o777, exist_ok=False)

    storage_client = storage.Client.from_service_account_json('/home/forde_a_smith/vannarho-fb3267082c74.json')

    risk_engine = RiskEngine(sys.argv[1] if len(sys.argv)>1 else False)
    risk_engine.risk_exe = '/home/forde_a_smith/risk_engine/build/App/ore'

# download params for counterparty
    bucket_name = 'risk_params'
    prefix = job_date + '/' + cpty + '/'
# prefix = '09-10-20/cpty_01/'
    dl_dir = './Input/'
    get_input_blobs(bucket_name,prefix,dl_dir,storage_client)

# download params for market
    bucket_name = 'market_params'
    prefix = job_date + '/'
    dl_dir = './Market/'
    get_input_blobs(bucket_name,prefix,dl_dir,storage_client)

# run risk analytics
    risk_engine.print_headline("Run risk engine to produce NPV cube and exposures")
    risk_engine.run("Input/ore.xml")
    # risk_engine.get_times("Output/log.txt")

# upload risk output files
    bucket_name = 'cpty_risk_outputs'
# destination_blob_name = '09-10-20/cpty_01/'
    destination_blob_name = job_date + '/' + cpty + '/'
    source_dir = './Output/'
# source_dir = '/risk_run/Output/'
    upload_blob(bucket_name, source_dir, destination_blob_name,storage_client)


if __name__ == "__main__":
    job_date = sys.argv[1]
    cpty = sys.argv[2]
    main(job_date, cpty)