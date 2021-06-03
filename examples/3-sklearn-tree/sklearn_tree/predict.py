"""
Predict
=======
Functions used to load models at prediction time and produce model decisions.
"""
from __future__ import print_function

import pickle
import functools

import numpy as np
from sklearn_tree import paths


@functools.lru_cache()
def load_model():
    """
    Load the pickled model back into memory. Since loading models can be
    expensive, this function is cached so that the model only needs to be loaded
    into memory once.

    Returns:
        model (sklearn.tree.DecisionTreeClassifier): The trained decision tree.
    """
    with open(paths.model('model.pkl'), 'rb') as stream:
        return pickle.load(stream)


def main(payload):
    """
    Run the decision tree classifier on the input payload. It is expected that
    the payload will have an 'age' and 'height' key, otherwise an error will
    occur.

    Note: This is the prediction entrypoint used by baklava!

    Arguments:
        payload (dict[str, object]): This is the payload that will eventaully
            be sent to the server using a POST request.

    Returns:
        payload (dict[str, object]): The output of the function is expected to
            be either a dictionary (like the function input) or a JSON string.
    """

    # Extract parameters from input dictionary
    age = payload['age']
    height = payload['height']

    # Load the model and execute
    model = load_model()
    x = np.array([[age, height]])  # Model expects matrix
    weights = model.predict(x)
    weight = int(weights[0])  # Model produces vector

    # Return back a payload with the result
    result = {'weight': weight}
    return result
