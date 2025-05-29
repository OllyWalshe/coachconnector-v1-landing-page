# CoachConnector Lead Capture MVP Project

**Goal** Build a fully functional MVP lead capture landing page using AWS services

## Project Overview

CoachConnector is a platform that matches clients with health and fitness coaches.
This project is Phase 1 of a multi-phase project to build and launch an Minimal Viable Product for this business within the cloud using AWS services.

**Stack Used**
- 

### Step 1 - DynamoDB Setup

**Goal** Set up a NoSQL datbase to store coach leads names, emails and coaching style with their email as a unique identifier.

**Services Used**
- AWS DynamoDB
**Actions**

- Created a table named 'CoachConnectorLeads'
    - Primary key: 'Email'
    
## Step 2 - Backend logic with AWS Lambda

**Goal** Develop a serverless backend function to revieve lead data from the frontend, validate it and store it in the DynamoDB table.

**Services Used**
- AWS Lambda
- Amazon DynamoDB
- AWS IAM

**Actions**
1. Created a new Lambda function using Python 3.9 runtime
2. Configured the Lambda function to have read/write permisiions for the DynamoDB table with IAM role
3. Wrote Python code in VS Code to:
    - Parse incoming JSON payload from the event
    - Validate required fields (name, email)
    - Insert the lead data into DynamoDB using put.item()
4. Tested the funtion via the AWS Console by creating a test event to simulate frontend payloads with the required fields.
    - Debugged and resolved issue related to case sensitivity of partition key (email vs Email)