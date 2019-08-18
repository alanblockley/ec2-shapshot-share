#!/bin/bash

sam package --template-file template.yaml --output-template-file ec2-snapshot-share.yaml --s3-bucket your-s3-bucket
aws cloudformation deploy --template-file /Users/alan.blockley/Documents/Projects/AWS/313/sam-app/ec2-snapshot-share.yaml --stack-name ec2-snapshot-share --capabilities CAPABILITY_IAM --region ap-southeast-2
