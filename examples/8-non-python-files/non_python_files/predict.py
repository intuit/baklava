"""
Predict
=======
Functions used to load models at prediction time and produce model decisions.
"""
from __future__ import print_function

import pickle
import pkgutil
import json

import numpy as np
from non_python_files import paths


class cache(object):
    """
    Simplified replacement of functools.lur_cache for python 2.7

    Use functools.lru_cache in any version of python > 3.5
    """
    def __init__(self, func):
        self.func = func
        self.result = None

    def __call__(self, *args, **kwargs):
        if self.result:
            return self.result
        self.result = self.func()
        return self.result


@cache
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


@cache
def load_thresholds():
    """
    Load the minimum and maximum age thresholds

    Returns:
        tuple:
            min_age (int): The minimum age to consider
            max_age (int): The maximum age to consider
    """
    content = pkgutil.get_data('non_python_files.resources', 'thresholds.json')
    mapping = json.loads(content)
    return mapping['min_age'], mapping['max_age']


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

    # Return unknown weight if outside of normal ranges
    min_age, max_age = load_thresholds()
    if age > max_age:
        return {'weight': 'Unknown'}

    if age < min_age:
        return {'weight': 'Unknown'}

    # Load the model and execute
    model = load_model()
    x = np.array([[age, height]])  # Model expects matrix
    weights = model.predict(x)
    weight = int(weights[0])  # Model produces vector

    # Return back a payload with the result
    result = {'weight': weight}
    return result
