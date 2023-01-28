import get_data
import aws

# download data
get_data.get_data()

# push data to s3
aws.push_to_s3()