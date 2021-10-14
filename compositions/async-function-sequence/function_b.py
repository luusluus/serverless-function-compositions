import os
from compose import compose

def lambda_handler(event, context):
    function_name = os.path.basename(__file__).split('.')[0]

    event['greet'] = event['greet'] + f'Hello world from {function_name}. '
    response = compose(function_name='AsyncSequenceFunctionC', data=event)
    return response