
import os
from compose import compose

def lambda_handler(event, context):
    function_name = os.path.basename(__file__).split('.')[0]
    event['greet'] = f'Hello world from {function_name}. '
    return compose(function_name='SequenceFunctionB', data=event)