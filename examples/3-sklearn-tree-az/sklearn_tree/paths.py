"""
Paths
=====
Define SageMaker path locations for both training and prediction containers.

https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo.html
"""
import os
from pathlib import Path
# from azureml.core import Dataset, Run
from io import StringIO
import pandas as pd

def initTraining():
    """
    Make folder paths for data, models, checkpoints
    """
    Path('/opt/ml/model/').mkdir(parents=True, exist_ok=True)

    # data_directories = {
    #     'training': "AIP_TRAINING_DATA_URI",
    #     'validation': "AIP_VALIDATION_DATA_URI",
    #     'testing': "AIP_TEST_DATA_URI"
    # }
    # key_file = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    # os.system(f'gcloud auth activate-service-account --key-file {key_file}')
    # for key in data_directories:

    #     # copy the folders to local
    #     gs_uri = os.getenv(data_directories[key])
    #     Path('/opt/ml/input/data/{key}/').mkdir(parents=True, exist_ok=True)
    #     os.system(f'gsutil -m cp -r {gs_uri} /opt/ml/input/data/{key}/')
        
    #     if os.getenv('AIP_DATA_FORMAT') == 'csv':
    #         os.system(f'cat * > {key}.csv')


def model(filename):
    """
    The path to model artifacts.

    Copies from GCS using GCP vertex environment variables 

    Arguments:
        filename (str): The name of the file which will be written back to S3

    Returns:
        path (str): The absolute path to the model output directory
    """
    model_uri = os.environ.get('AZUREML_MODEL_DIR')
    return os.path.join(model_uri, filename)


def input(channel, filename):
    """
    The path to input artifacts.

    Amazon SageMaker allows you to specify "channels" for your docker container.
    The purpose of a channel is to copy data from S3 to a specified directory.

    Amazon SageMaker makes the data for the channel available in the
    /opt/ml/input/data/channel_name directory in the Docker container.

    For example, if you have three channels named training, validation, and
    testing, Amazon SageMaker makes three directories in the Docker container:

        /opt/ml/input/data/training
        /opt/ml/input/data/validation
        /opt/ml/input/data/testing

    Arguments:
        channel (str): The name of the channel which contains the given filename
        filename (str): The name of the file within a specific channel

    Returns:
        path (str): The absolute path to the specified channel file
    """
    return os.path.join(os.sep, 'opt', 'ml', 'input', 'data', channel, f'{channel}.csv')


def inputAsDataframe(channel: str, filename=None):
    """
    The path to input artifacts.

    Amazon SageMaker allows you to specify "channels" for your docker container.
    The purpose of a channel is to copy data from S3 to a specified directory.

    Amazon SageMaker makes the data for the channel available in the
    /opt/ml/input/data/channel_name directory in the Docker container.

    For example, if you have three channels named training, validation, and
    testing, Amazon SageMaker makes three directories in the Docker container:

        /opt/ml/input/data/training
        /opt/ml/input/data/validation
        /opt/ml/input/data/testing

    Arguments:
        channel (str): The name of the channel which contains the given filename
        filename (str): The name of the file within a specific channel

    Returns:
        path (str): The absolute path to the specified channel file
    """

    # channel --> environmental variable names
    data_directories = {
        'training': "training-data",
        'validation': "validation-data",
        'testing': "testing-data"
    }

    if channel in data_directories.keys():
        azure_mount_file = os.environ.get(data_directories[channel])
        print(f'azure_mount_file={azure_mount_file}')
        data = pd.read_csv(azure_mount_file)
        return data
        # run = Run.get_context()
        # print(run)

        # if(run.experiment):
        #     ws = run.experiment.workspace
        #     # get the input dataset by ID
        #     dataset = Dataset.get_by_id(ws, id=os.environ.get(f'{channel}-data'))

        #     # load the TabularDataset to pandas DataFrame
        #     df = dataset.to_pandas_dataframe()
        #     return df
        # else:

    else:
        print('Incorrect data channel type. Options are training, validation, and testing.')
        return null

def failure():
    """
    The path to the failure file.

    If training fails, after all algorithm output (for example, logging)
    completes, your algorithm should write the failure description to this file.

    Returns:
        path (str): The absolute path to the failure file
    """
    return os.path.join(os.sep, 'opt', 'ml', 'output', 'failure')


def output(filename):
    """
    The path to the output artifacts.

    Your algorithm should write all final model artifacts to this directory.
    Amazon SageMaker copies this data as a single object in compressed tar
    format to the S3 location that you specified in the CreateTrainingJob
    request. If multiple containers in a single training job write to this
    directory they should ensure no file/directory names clash. Amazon SageMaker
    aggregates the result in a tar file and uploads to S3.

    Arguments:
        filename (str): The name of the file which will be written back to S3

    Returns:
        path (str): The absolute path to the model output directory
    """
    Path('/.outputs/model').mkdir(parents=True, exist_ok=True)
    return os.path.join(os.sep, '.outputs', 'model', filename)

def outputUpload():
    """
    Copies files in local model directory to google storage

    """
    # storage_client = storage.Client()
    # bucket_uri = os.getenv('AIP_MODEL_DIR')
    # bucket_name, prefix = getBucketNameFrom(bucket_uri)
    # # blob = bucket.blob('model.pkl')
    # # artifact = f'{bucket_uri}/model.pkl'

    # bucket = storage_client.bucket(bucket_name)
    # for filename in os.listdir('/opt/ml/model/'):
    #     print(filename)
    #     blob = bucket.blob(prefix + '/' + filename)
    #     blob.upload_from_filename('/opt/ml/model/' + filename)


def config():
    """
    The path to all SageMaker configuration files.

    The directory where standard SageMaker configuration files are located
    SageMaker training creates the following files in this folder when training
    starts:

        - `hyperparameters.json`: Amazon SageMaker makes the hyperparameters in
            a CreateTrainingJob request available in this file.
        - `inputdataconfig.json`: You specify data channel information in the
            InputDataConfig parameter in a CreateTrainingJob request. Amazon
            SageMaker makes this information available in this file.
        - `resourceconfig.json`: The name of the current host and all host
            containers in the training

    Returns:
        path (str): The absolute path to the config directory
    """
    return os.path.join(os.sep, 'opt', 'ml', 'input', 'config')


def hyperparameters():
    """
    The path to the model hyperparameter configuration file.

    Amazon SageMaker makes the hyperparameters in a CreateTrainingJob request
    available in this file.

    Returns:
        path (str): The absolute path to the hyperparameters JSON
    """
    return os.path.join(config(), 'hyperparameters.json')


def input_data_config():
    """
    The path to the input data configuration file.

    You specify data channel information in the InputDataConfig parameter in a
    CreateTrainingJob request. Amazon SageMaker makes this information available
    in this file.

    Returns:
        path (str): The absolute path to the input data config JSON
    """
    return os.path.join(config(), 'inputdataconfig.json')


def resource_config():
    """
    The path to the resource configuration file.

    A file containing the name of the current host and all host containers in
    the training.

    Returns:
        path (str): The absolute path to the resource config JSON
    """
    return os.path.join(config(), 'resourceconfig.json')

#TODO: Missing checkpoint function
# GCP requires an upload step of the checkpoint. Outstanding question of when to run the upload call.


def initPrediction():
    """
    Make folder paths for models and download from GS
    """
    Path('/opt/ml/model/').mkdir(parents=True, exist_ok=True)

    storage_client = storage.Client()

    bucket_name = os.getenv('AIP_STORAGE_URI')
    bucket = storage_client.bucket(bucket_name)
    # blob = bucket.blob('model.pkl')
    artifact = f'{bucket_name}/model.pkl'
    print(f'GS Artifact location: {artifact}')
    blob = Blob.from_string(artifact, storage_client)
    blob.download_to_filename('/opt/ml/model/model.pkl')

def containerPort():
    return os.getenv('AIP_HTTP_PORT')

def modelId():
    return os.getenv('AIP_DEPLOYED_MODEL_ID')