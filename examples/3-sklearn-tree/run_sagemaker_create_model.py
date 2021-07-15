
import boto3
client = boto3.Session().client('sagemaker')

response = client.create_model(
    ModelName='stumblebum-lenitives',
    PrimaryContainer={
        'Image': '436885317446.dkr.ecr.us-east-1.amazonaws.com/mlctl-test:predict-image',
        'ImageConfig': {
            'RepositoryAccessMode': 'Platform',
        },
        'Mode': 'SingleModel',
        'ModelDataUrl': 's3://mlctltest/example1_output/mlctl-stumblebum-lenitives/output/model.tar.gz',
        'Environment': {
            'sriracha_provider': 'awssagemaker'
        },
    },
    ExecutionRoleArn='arn:aws:iam::436885317446:role/sm-execution',
    Tags=[
        {
            'Key': 'mlctl',
            'Value': 'asdf'
        },
    ]
)

print(response)

response = client.create_endpoint_config(
    EndpointConfigName='stumblebum-lenitives-endpoint-config',
    ProductionVariants=[
        {
            'VariantName': 'main',
            'ModelName': 'stumblebum-lenitives',
            'InitialInstanceCount': 1,
            'InstanceType': 'ml.t2.medium',
            'InitialVariantWeight': 1.0,
        },
    ],
    # DataCaptureConfig={
    #     'EnableCapture': True|False,
    #     'InitialSamplingPercentage': 123,
    #     'DestinationS3Uri': 'string',
    #     'KmsKeyId': 'string',
    #     'CaptureOptions': [
    #         {
    #             'CaptureMode': 'Input'|'Output'
    #         },
    #     ],
    #     'CaptureContentTypeHeader': {
    #         'CsvContentTypes': [
    #             'string',
    #         ],
    #         'JsonContentTypes': [
    #             'string',
    #         ]
    #     }
    # },
    Tags=[
        {
            'Key': 'mlctl',
            'Value': 'asdf'
        },
    ],
)

print(response)