import json
import boto3
from botocore.exceptions import ClientError


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CoachConnectorLeads')


def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])

        name = data.get('name')
        email = data.get('email')
        style = data.get('style')

        if not email or not name:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Missing name or email'})
            }
        
        response = table.put_item(
            Item={
                'email': email,
                'name': name,
                'style': style
            }
        )


        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Lead added successfully'})
        }
    
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
    
    