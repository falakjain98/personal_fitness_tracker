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


### AWS EC2 instance setup - to extract data from Google Sheets to AWS S3
