
import boto3
client = boto3.Session().client('sagemaker')

response = client.create_endpoint(
    EndpointName='stumblebum-lenitives-endpoint',
    EndpointConfigName='stumblebum-lenitives-endpoint',
    Tags=[
        {
            'Key': 'mlctl',
            'Value': 'asdf'
        },
    ]
)

print(response)