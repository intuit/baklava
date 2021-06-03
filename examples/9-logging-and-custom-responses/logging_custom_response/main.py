from __future__ import print_function

import logging
import functools


logger = logging.getLogger('baklava')


@functools.lru_cache()
def load_model():
    """
    Example initializer which contains logging

    Returns:
        result (int): A constant value to use a the model
    """
    logger.info('load_model called')
    return 1


def hosted_function(payload):
    """
    Example hosted function which always returns a 201 with the message "OK".
    This uses a tuple return type containing the status code which is directly
    supported by Flask.

    See: https://flask.palletsprojects.com/en/1.1.x/quickstart/#about-responses

    Arguments:
        payload (dict[str, object]): This is the payload that will eventually
            be sent to the SageMaker server using a POST request to the
            `invocations` route.

    Returns:
        response (tuple[str, int]):
            message (str): The response message.
            status (int): The status code.
    """
    logger.info('hosted_function called')
    return 'OK', 201
