# Personal Fitness Tracker

### Project Summary

A pipeline to actively extract data from my fitness tracker and visualize fitness metrics and insights

The following technologies are utilized in this project:
- [AWS Services](https://aws.amazon.com/): *Cloud platform*
  - [EC2](https://aws.amazon.com/ec2/?nc2=h_ql_prod_fs_ec2): *Virtual Machine*
  - [S3](https://aws.amazon.com/s3/?nc2=h_ql_prod_fs_s3): *Data Storage*
  - [RDS](https://aws.amazon.com/rds/?nc2=h_ql_prod_fs_rds): *Database*
  - [Lambda](https://aws.amazon.com/lambda/): *Servless Function to Transfer Data from Storage to Database*
- [Python (via Anaconda)](https://www.anaconda.com/products/distribution): *Programming Language*

The entirety of this project is deployed using the AWS Free Tier, some Apple Apps and an Amazfit fitness tracker that I own

### Project Architecture

<img width="900" alt="image" src="https://user-images.githubusercontent.com/54712290/215236846-e726d138-92d1-446e-a966-2ca03e28c450.png">

### Dashboard

The dashboard which utilizes this pipeline can be viewed at https://lookerstudio.google.com/reporting/442ccfa2-0407-44b2-ba12-766d30b29c1c

<img width="900" alt="image" src="https://user-images.githubusercontent.com/54712290/215350640-aef6828e-81f5-4e1f-9f70-8865d11317af.png">

### Setup & Deploy
Please refer to [setup](setup.md) file for more details regarding infrastructure setup.

After setup, deploy the pipeline using steps on the [deploy](deploy.md) file.

### Learn More
To learn more about Data and Analytics Engineering, check out [DataTalksClub's](https://github.com/DataTalksClub) amazing [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp)!

Link to my report from their Data Engineering Zoomcamp: [Taxi Trips Data](https://datastudio.google.com/reporting/d9c8aab0-4ab9-4acf-9444-0135a1eda5ae)
