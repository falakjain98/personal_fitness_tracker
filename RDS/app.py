import sys
import logging
import pymysql
import boto3

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

# Read CSV file content from S3 bucket
def read_data_from_s3(event):
    bucket_name = 'apple-health-data'
    s3_file_name = 'steps.csv'
    resp = s3_cient.get_object(Bucket=bucket_name, Key=s3_file_name)

    data = resp['Body'].read().decode('utf-8')
    data = data.split("\n")
    return data

def handler(event, context):
    logger.info("Reading Data")
    data = read_data_from_s3(event)
    logger.info("Data Read Successful")
    with conn.cursor() as cur:
        #cur.execute("drop table steps")
        cur.execute("create table IF NOT EXISTS steps (timestamp DATETIME NOT NULL, steps FLOAT NOT NULL)")
        for emp in data: # Iterate over S3 csv file content and insert into MySQL database
            try:
                emp = emp.replace("\n","").split(",")
                print (">>>>>>>"+str(emp))
                cur.execute('insert into steps (timestamp,steps) values("'+str(emp[0])+'","'+str(emp[1])+'")')
                conn.commit()
            except:
                continue
        cur.execute("select count(*) from steps")
        print ("Total records on DB :"+str(cur.fetchall()[0]))
        # Display employee table records
        # for row in cur:
        #     print (row)
    if conn:
        conn.commit()
        
handler()