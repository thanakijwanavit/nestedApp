import json
import pandas as pd

# import requests


def lambda_handler(event, context):
    pd.DataFrame({'hello':[1,2], 'world':[3,4]})
    print('hello')

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
