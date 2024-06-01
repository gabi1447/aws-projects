import boto3
import json

get_method = "GET"
status_path = "/status"
transactions_path = "/transactions"


def lambda_handler(event, context):
    http_method = event["httpMethod"]
    path        = event["path"]
    
    if http_method == get_method and path == transactions_path:
        transaction_id = event["queryStringParameters"]["transaction_id"]
        transaction_amount = event["queryStringParameters"]["transaction_amount"]
        transaction_date = event["queryStringParameters"]["transaction_date"]
    
        response = {
            "transaction_id": transaction_id,
            "transaction_amount": transaction_amount,
            "transaction_date": transaction_date,
            "message"         : "Welcome to Lambda!"
        }
        
    elif http_method == get_method and path == status_path:
        response = {
            "message": "The API is up and running"
            }
    
    return {
        "statusCode": 200,
        "headers"   : {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response)
    }
