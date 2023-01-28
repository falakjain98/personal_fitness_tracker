import boto3
import json
import os
from botocore.exceptions import ClientError
import logging
import config
import psycopg2

def push_to_s3():
    s3_client = boto3.client('s3')
    for i in config.sheet_links.keys():
        s3_client.upload_file(f'health_data/{i}.csv',config.aws_bucket_name,f'{i}.csv')