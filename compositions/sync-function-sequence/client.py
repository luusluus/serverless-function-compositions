

import json
from boto3 import client as boto3_client
from compositions.aws_helpers.s3 import S3BucketHelper


aws_region = 'eu-central-1'
client = boto3_client('lambda', region_name=aws_region)

# call the first function a to start the workflow
response = client.invoke(
    FunctionName='SequenceFunctionA',
    InvocationType='RequestResponse'
)

if response['StatusCode'] == 200:
    result = json.load(response['Payload'])
    print(result['result'])



