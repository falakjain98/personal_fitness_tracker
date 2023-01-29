import sys
import logging
import pymysql
import boto3
import config

s3_cient = boto3.client('s3')

#rds settings
rds_host  = config.rds['endpoint']
name = config.rds['username']
password = config.rds['password']
db_name = config.rds['database_name']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

bucket_name = 'apple-health-data'
file_names = {'steps':'steps.csv',
                'resting_energy':'resting_energy.csv',
                'active_energy':'active_energy.csv',
                'heart_rate':'heart_rate.csv',
                'distance':'distance.csv'}

# Read CSV file content from S3 bucket
def read_data_from_s3(event,bucket_name,s3_file_name):
    resp = s3_cient.get_object(Bucket=bucket_name, Key=s3_file_name)
    data = resp['Body'].read().decode('utf-8')
    data = data.split("\n")
    return data

def handler(event, context):
    with conn.cursor() as cur:
        for key,file in file_names.items():
            data = read_data_from_s3(event,bucket_name,file)
            count = 0
            #cur.execute("drop table steps")
            cur.execute(f"create table IF NOT EXISTS {key} (timestamp DATETIME NOT NULL, {key} FLOAT NOT NULL, PRIMARY KEY (timestamp))")
            for rec in data: # Iterate over S3 csv file content and insert into MySQL database
                try:
                    rec = rec.replace("\n","").split(",")
                    cur.execute(f'insert ignore into {key} (timestamp,{key}) values("'+str(rec[0])+'","'+str(rec[1])+'")')
                    count+=1
                    conn.commit()
                except:
                    continue
            print(f"Wrote {count} records to {key} table")
            cur.execute(f"select count(distinct timestamp) from {key}")
            print (f"Total records in {key} table  :"+str(cur.fetchall()[0]))
    if conn:
        conn.commit()