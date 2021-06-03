from __future__ import print_function

import time
import functools


@functools.lru_cache()
def load_model():
    """
    This is an example function which takes a long time to load. In some cases
    models will need many seconds or minutes to load into memory. Rather than
    waiting for a model to load on the first function call, this function can
    be called immediately after the python process has been started. See the
    `setup.py` file for the initialization call.

    In this example, the "model" is just a constant number, but this could be
    any python object.

    Returns:
        result (int): A constant value to use a the model
    """
    print('Running Slow Load Function!')
    time.sleep(5)  # Artificial 5 second penalty to loading the model
    return 1


def predict(payload):
    """
    Define a hosted function that echos out the input. When creating a
    predict image, this is the function that is hosted on the invocations
    endpoint.

    This function just adds 1 to any object in the payload if it is possible

    Arguments:
        payload (dict[str, object]): This is the payload that will eventually
            be sent to the SageMaker server using a POST request to the
            `invocations` route.

    Returns:
        payload (dict[str, object]): The output of the function is expected to
            be either a dictionary (like the function input) or a JSON string.
    """

    print('Loading model...', end='')
    model = load_model()
    print('Done.')

    for key, value in payload.items():
        try:
            payload[key] = int(value) + model
        except ValueError:
            pass  # Do nothing if value can't be casted to int

    return payload

