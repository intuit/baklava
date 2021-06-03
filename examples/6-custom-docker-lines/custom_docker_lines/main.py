from __future__ import print_function


def training_function():
    """
    Define a training function that just prints out to stdout. Training jobs
    do not take any arguments as input and do not need to return anything.

    Note that the function can be named anything as long as it is correctly
    referenced in the setup.py
    """
    print('Hello World')


def hosted_function(payload):
    """
    Define a hosted function that echos out the input. When creating a
    predict image, this is the function that is hosted on the invocations
    endpoint.

    Arguments:
        payload (dict[str, object]): This is the payload that will eventually
            be sent to the SageMaker server using a POST request to the
            `invocations` route.

    Returns:
        payload (dict[str, object]): The output of the function is expected to
            be either a dictionary (like the function input) or a JSON string.
    """
    return payload

