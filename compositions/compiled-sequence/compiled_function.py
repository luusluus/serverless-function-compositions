from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

def function_a():
    return f'Hello world from {function_a.__name__}. '

def function_b():
    return f'Hello world from {function_b.__name__}. '

def function_c():
    return f'Hello world from {function_c.__name__}. '

def lambda_handler(event, context):
    subsegment = xray_recorder.begin_subsegment('Business Logic')
    subsegment.put_annotation('workflow_instance_id', event['workflow_instance_id'])
    result = function_a() + function_b() + function_c()
    xray_recorder.end_subsegment()
    
    return result