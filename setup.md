# Set up your own live fitness tracking pipeline

### 1. Sync your fitness tracker with Apple Health

<img width="200" alt="image" src="https://user-images.githubusercontent.com/54712290/215351602-de89df6a-8d8d-4748-8e06-90247a50d235.png">

### 2. Set up Google App Script - API call to push input data to a Google Sheet

- [Google App Script](https://developers.google.com/apps-script/overview) is an application development platform to create applications that integrate with Google Workspace
- Set up a script to listen to incoming data via API calls and push it to a Google Sheet in the following manner
<img width="900" alt="image" src="https://user-images.githubusercontent.com/54712290/215352216-35091095-7bcb-41ee-9a5c-c465af42756a.png">
- The whitened out portion shall include your Google Sheet's ID
- Create another script to clear all the Google Sheets to remove redundant data in the following manner
<img width="900" alt="image" src="https://user-images.githubusercontent.com/54712290/215352540-b5a8540a-34b3-49cb-a236-3a3a3ae6cacb.png">
- Create similar listeners for distance, active energy, heart rate, etc. to push your data to a Google Sheet
- Deploy all the scripts and store the Deployment IDs for later

### 3. Set up Apple Shortcuts - to retrieve fitness data from the Health app and push to Google Sheet

- Create the following automation from the Shortcuts app from your iPhone using several chained actions
<img width="200" alt="image" src="https://user-images.githubusercontent.com/54712290/215352894-f3616d23-cf02-4862-ba53-e67874d9e107.png">
- This is what the 'Clear Sheets' action should look like
<img width="200" alt="image" src="https://user-images.githubusercontent.com/54712290/215353164-6031aa3b-8f58-4823-898b-88da932ba4e8.png">
- This is what one of the 'Fitness Metric to GSheet' actions should look like
<img width="200" alt="image" src="https://user-images.githubusercontent.com/54712290/215358248-8d2246f0-41ac-421a-89c2-0830363733f0.png">
- We will create another action to trigger the python script in the VM via SSH later in the set up.

### 4. AWS EC2 instance setup - to extract data from Google Sheets to AWS S3

- Set up an (AWS EC2 instance)[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html] to run the Python script which downloads data from Google Sheets and pushes it to S3
- I have used the free tier for setting up my EC2 instance and find it to be enough to run this project
- SSH into your EC2 instance and clone with Git repo
- Install [Anaconda for Linux](https://www.anaconda.com/products/distribution)
  - Use wget to download latest Anaconda version for Linux
  - Run the executable file with `bash file-name.sh` command
  - Log out and log back in using ```source .bashrc``` to complete installation
- Create `config.py` and `RDS/config` files similar to the `config_example.py` and `RDS/config_example.py` files
- `pip install` required libraries used in the python scripts: `subprocess`,`boto3`,`psycopg2`,`botocore`

### 5. Create RDS MySQL database
- I used the AWS free tier to create my database instance
- Store database credentials in `RDS/config.py` file in order to successfully run Lambda functions

### 6. Create an S3 bucket to upload csv files to
- Create an S3 bucket with a suitable name and update the AWS.py file accordingly

### 7. Set up Lambda function - function to transfer files from S3 to RDS when a file is updated
- Create a new Lambda function with a name you prefer
- Zip the contents of the `RDS` folder and upload to the Lambda function
- This is the [resource that I referred to](https://github.com/prabhakar2020/insert_s3_csv_file_content_to_mysql_using_lambda)
- Add an S3 trigger to your Lambda function so that the function runs whenever objects in S3 are updated
- You can test your Lambda function to ensure data reads and database updates
- This is what my Lambda function looks like:
<img width="900" alt="image" src="https://user-images.githubusercontent.com/54712290/215379041-2df3fbfc-eece-4faf-903a-33d4afe92950.png">

### 8. Create a 'Run Script Over SSH' Action
- This action allows the python scripts to be run in the EC2 instance, from the convenience of your own phone
- You will have the configure the Action with the public IP of your VM as well as the username
- [Store the SSH key created by your Action in `~/.ssh/authorized_kays` file on EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/replacing-key-pair.html)
- In Script, enter `/home/ubuntu/anaconda3/bin/python personal_fitness_tracker/ingest_transform_s3.py`
<img width="200" alt="image" src="https://user-images.githubusercontent.com/54712290/215380534-d88dc1cf-3d3b-4cd5-9e83-0c0dfb009a8b.png">

- Add this action to the automation we created in step 3

### 9. [Optional] Connect BI tool to RDS database to vizualize constantly updating data
- I chose to connect a Google Data Studio report to the RDS instance and [visualize the data in this manner](https://lookerstudio.google.com/reporting/442ccfa2-0407-44b2-ba12-766d30b29c1c)
- However, this step is optional and completely user dependent based on BI tool preferences

### 10. Run complete pipeline
- This concludes the pipeline setup, you can play the automation from your phone at the click of a button on a daily basis to ensure up to date data is stored in your RDS instance
- While I recommend a daily run, the Apple Shortcuts extracts data for the last 2 days to ensure no data points are missed. Even if a data point is captured on 2  consecutive days, duplicates are removed when writing to the database to ensure accurate results!

