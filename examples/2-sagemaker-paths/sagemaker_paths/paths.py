"""
Paths
=====
Define SageMaker path locations for both training and prediction containers.

https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo.html
"""
import os


def model(filename):
    """
    The path to model artifacts.

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
    return os.path.join(os.sep, 'opt', 'ml', 'input', 'data', channel, filename)


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
