import json
import boto3

dynamo = boto3.resource("dynamodb")
table  = dynamo.Table('planets')

def lambda_handler(event, context):
    response = table.get_item(
            Key={
                "id": "mercury"
            }
    )
    return {
        "statusCode": 200,
        "body"      : response["Item"]
    }
