import json
import boto3
import os

# import requests


def lambda_handler(event, context):

    ec2_client = boto3.client('ec2', region_name='ap-southeast-2')

    SnapshotArn = event['resources'][0]
    SnapshotList = SnapshotArn.split("/")

    response = ec2_client.modify_snapshot_attribute(
        Attribute='createVolumePermission',
        CreateVolumePermission={
            'Add': [
                {
                    'UserId': os.environ['DEST_ACCOUNT']
                },
            ]
        },        
        SnapshotId=SnapshotList[1],   
    )

    print("Snapshot", SnapshotList[1])

    print(event)
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Shared " + SnapshotList[1] + " to account " + os.environ['DEST_ACCOUNT']
        }),
    }
