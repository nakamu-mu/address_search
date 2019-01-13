from chalice import Chalice
import boto3
import json

BUCKET_NAME = 'address-search-test'
s3 = boto3.client('s3')

app = Chalice(app_name='address_search')


@app.lambda_function()
def handler(event, contet):
    if event.get('postal_code') is None:
        return {'data': 'postal_code is None'}
    
    expression = "Select _3, _7, _8, _9 from S3Object s where s._3='{}'".format(event.get('postal_code'))
    select_result = s3.select_object_content(
        Bucket = BUCKET_NAME,
        Key = 'x-ken-all.csv',
        ExpressionType = 'SQL',
        Expression = expression,
        InputSerialization = {
            'CSV': {
                'FileHeaderInfo': 'NONE',
                'RecordDelimiter': '\n',
                'FieldDelimiter': ',',
            }
        },
        OutputSerialization = {
            'CSV': {
                'RecordDelimiter': '\n',
                'FieldDelimiter': ',',
            }
        },
    )
    records = []
    for event in select_result['Payload']:
        if 'Records' in event:
            records.append(event['Records']['Payload'].decode('utf-8'))
    return {'records': records, 'expression': expression}
