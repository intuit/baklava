"""
Predict
=======
Functions used to load models at prediction time and produce model decisions.
"""
from __future__ import print_function

import functools

import numpy as np
import tensorflow as tf

from tensorflow_mnist import model, paths


@functools.lru_cache()
def load_model():
    """
    Load the saved model variables back into memory. Since loading models can be
    expensive, this function is cached so that the model only needs to be loaded
    into memory once.
    """

    # Recreate the model graph
    graph, x, y, step, initializer, accuracy, prediction = model.build()

    # Create a session which will hold variable state in memory
    session = tf.Session(graph=graph)
    path = paths.model('mnist')

    with graph.as_default():
        saver = tf.train.Saver()

        # Restore the graph variable state
        saver.restore(session, path)

    return session, x, prediction


def main(payload):
    """
    Run the tensorflow model on the input payload. It is expected that
    the payload will have a `data` node which contains pixel intensities

    Note: This is the prediction entrypoint used by baklava!

    Arguments:
        payload (dict[str, object]): This is the payload that will eventaully
            be sent to the server using a POST request.

    Returns:
        payload (dict[str, object]): The output of the function is expected to
            be either a dictionary (like the function input) or a JSON string.
    """

    # Extract parameters from input dictionary
    if 'data' not in payload:
        inputs = [0] * 784
    else:
        inputs = payload['data']

    data = np.array(inputs).reshape(1, 784)

    # Load model session and interface
    session, x, prediction = load_model()

    # Compute prediction
    prediction = int(session.run(prediction, feed_dict={x: data}))

    # Return back a payload with the result
    result = {'prediction': prediction}
    return result
