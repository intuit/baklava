"""
Paths
=====
Define SageMaker path locations for both training and prediction containers.

https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo.html
"""
import os
from pathlib import Path
from google.cloud import storage


def init():
    """
    Make folder paths for data, models, checkpoints
    """
    Path('/opt/ml/model/').mkdir(parents=True, exist_ok=True)

def model(filename):
    """
    The path to model artifacts.

    Copies from GCS using GCP vertex environment variables 

    Arguments:
        filename (str): The name of the file which will be written back to S3

    Returns:
        path (str): The absolute path to the model output directory
    """
    bucket_name = os.getenv('AIP_STORAGE_URI')
    client = storage.Client()
# https://console.cloud.google.com/storage/browser/[bucket-id]/
    bucket = client.get_bucket(bucket_name)

    # hardcore model.pkl, but production code should be packaged as a dynamic copy of all files in directory
    blob = bucket.blob('model.pkl')
    blob.download_to_filename('/opt/ml/model')

    return os.path.join(os.sep, 'opt', 'ml', 'model', filename)


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
    data_directories = {
        'training': "AIP_TRAINING_DATA_URI",
        'validation': "AIP_VALIDATION_DATA_URI",
        'testing': "AIP_TESTING_DATA_URI"
    }
    if channel in data_directories:
        client = storage.Client()

        gs_uri = data_directories[channel]
        bucket = client.get_bucket(os.getenv(gs_uri))
        blob = bucket.blob(filename)

        Path('/opt/ml/input/data/' + channel).mkdir(parents=True, exist_ok=True)
        blob.download_to_filename('/opt/ml/input/data/' + channel + '/' + filename)
        return os.path.join(os.sep, 'opt', 'ml', 'input', 'data', channel, filename)
    else:
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
    return os.path.join(os.sep, 'opt', 'ml', 'model', filename)

def outputUpload():
    """
    Copies files in local model directory to google storage

    """
    storage_client = storage.Client()
    bucket_name = os.getenv('AIP_MODEL_DIR')
    bucket = storage_client.bucket(bucket_name)
    for filename in os.listdir('/opt/ml/model/'):
        blob = bucket.blob(filename)
        blob.upload_from_filename('/opt/ml/model/' + filename)


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
