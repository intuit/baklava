"""
Predict
=======
Functions used to load models at prediction time and produce model decisions.
"""
from __future__ import print_function

import functools

from sagemaker_paths import paths


@functools.lru_cache()
def load_model():
    """
    Loads and caches the model data.

    Note: Using `functools.lru_cache` is good practice for long operations that
    you want to run only once. This is especially useful when loading model
    artifacts.

    Returns:
        content (str): The model string
    """
    path = paths.model('model.txt')
    with open(path, 'r') as stream:
        content = stream.read()
    return content


def main(payload):
    """
    Defines a hosted function that appends the model.txt text to the data
    parameter.

    Note: This is the prediction entrypoint used by baklava!

    Arguments:
        payload (dict[str, object]): This is the payload that will eventually
            be sent to the SageMaker server using a POST request to the
            `invocations` route.

    Returns:
        payload (dict[str, object]): The output of the function is expected to
            be either a dictionary (like the function input) or a JSON string.
    """

    data = payload['data']
    result = str(data) + load_model()
    payload['data'] = result
    return payload
