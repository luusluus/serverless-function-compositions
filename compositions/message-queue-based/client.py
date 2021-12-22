import json

from boto3 import client as boto3_client
from compositions.aws_helpers.s3 import S3BucketHelper


aws_region = 'eu-central-1'

client = boto3_client('lambda', region_name=aws_region)

response = client.invoke(
    FunctionName='MessageQueueProxyFunction',
    InvocationType='RequestResponse',
    Payload=json.dumps({
        'sleep': 2,
        'waiter_config': {
            'delay': 1,
            'max_attempts': 30
        },
        "message_attributes": {
                "caller": {
                    "DataType": "String",
                    "StringValue": "ProxyClient"
                },
                "last_function": {
                    "DataType": "String",
                    "StringValue": "MessageQueueFunctionC"
                }
            }
    })
)

if response['StatusCode'] == 200:
    print(response)
else:
    print('Composition Failed')