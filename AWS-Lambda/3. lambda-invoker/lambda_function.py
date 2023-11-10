import json
import boto3

# create a client to invoke the lambda function
client = boto3.client('lambda')


def lambda_handler(event, context):
    inputForInvoker = {
        'customer_id': '123456',
        'amount': 100
    }

    # invoke the lambda function
    response = client.invoke(
        FunctionName='arn:aws:lambda:us-east-2:460417962015:function:lambda_to_invoke',
        InvocationType='RequestResponse',  # Another option is Event
        Payload=json.dumps(inputForInvoker)  # convert python dict to json
    )

    # get the response from the invoked lambda function
    responseFromInvokedLambda = json.loads(response['Payload'].read())

    print('\n{}\n'.format(responseFromInvokedLambda))
