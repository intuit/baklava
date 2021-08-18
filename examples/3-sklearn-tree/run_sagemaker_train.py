from random_word import RandomWords
import boto3
client = boto3.Session().client('sagemaker')

words = RandomWords().get_random_words()
response = client.create_training_job(
    TrainingJobName=f'mlctl-{words[0]}-{words[1]}',
    # HyperParameters={
    #     'string': 'string'
    # },
    AlgorithmSpecification= {
      "TrainingImage": '436885317446.dkr.ecr.us-east-1.amazonaws.com/mlctl-test:train-image',
      "TrainingInputMode": "File"
    },
    RoleArn='arn:aws:iam::436885317446:role/sm-execution',
    InputDataConfig=[
        {
            'ChannelName': 'training',
            'DataSource': {
                'S3DataSource': {
                    'S3DataType': 'S3Prefix',
                    'S3Uri': 's3://mlctltest/example1_data/',
                    'S3DataDistributionType': 'FullyReplicated',
                }
            },
            'ContentType': 'text/csv',
            # 'CompressionType': 'None'|'Gzip',
            # 'RecordWrapperType': 'None'|'RecordIO',
            'InputMode': 'File',
            # 'ShuffleConfig': {
            #     'Seed': 123
            # }
        },
    ],
    OutputDataConfig={
        'S3OutputPath': 's3://mlctltest/example1_output/'
    },
    ResourceConfig={
        'InstanceType': 'ml.m5.large',
        'InstanceCount': 1,
        'VolumeSizeInGB': 5,
    },
    StoppingCondition={
        'MaxRuntimeInSeconds': 1800
    },
    Tags=[
        {
            'Key': 'mlctl',
            'Value': 'local'
        },
    ],
    # EnableManagedSpotTraining=True|False,
    # CheckpointConfig={
    #     'S3Uri': 'string',
    #     'LocalPath': 'string'
    # },
    # TensorBoardOutputConfig={
    #     'LocalPath': 'string',
    #     'S3OutputPath': 'string'
    # },
    # ExperimentConfig={
    #     'ExperimentName': 'mlctl_test',
    #     'TrialName': 'v1',
    #     'TrialComponentDisplayName': 'training_step'
    # },
    # ProfilerConfig={
    #     'S3OutputPath': 'string',
    #     'ProfilingIntervalInMilliseconds': 123,
    #     'ProfilingParameters': {
    #         'string': 'string'
    #     }
    # },
    # ProfilerRuleConfigurations=[
    #     {
    #         'RuleConfigurationName': 'string',
    #         'LocalPath': 'string',
    #         'S3OutputPath': 'string',
    #         'RuleEvaluatorImage': 'string',
    #         'InstanceType': 'ml.t3.medium'|'ml.t3.large'|'ml.t3.xlarge'|'ml.t3.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.r5.large'|'ml.r5.xlarge'|'ml.r5.2xlarge'|'ml.r5.4xlarge'|'ml.r5.8xlarge'|'ml.r5.12xlarge'|'ml.r5.16xlarge'|'ml.r5.24xlarge'|'ml.g4dn.xlarge'|'ml.g4dn.2xlarge'|'ml.g4dn.4xlarge'|'ml.g4dn.8xlarge'|'ml.g4dn.12xlarge'|'ml.g4dn.16xlarge',
    #         'VolumeSizeInGB': 123,
    #         'RuleParameters': {
    #             'string': 'string'
    #         }
    #     },
    # ],
    Environment={
        'sriracha_provider': 'awssagemaker'
    },
    # RetryStrategy={
    #     'MaximumRetryAttempts': 123
    # }
)

print(response)