import json
import uuid


def lambda_handler(event, context):
    # read off the event
    customer_id = event['customer_id']

    # generate a unique id
    transaction_id = str(uuid.uuid4())

    # do some work i.e. save to s3, write to database, etc.

    return {
        'customer_id': customer_id,
        'transaction_id': transaction_id,
        'Success': 'true'
    }
