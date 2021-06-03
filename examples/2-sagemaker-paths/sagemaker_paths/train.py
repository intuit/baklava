"""
Train
=====
Defines functions which train models and write model artifacts to disk.
"""
from __future__ import print_function

from sagemaker_paths import paths


def process(data):
    """
    Lower cases and reverses a string

    Arguments:
        data (str): The string to transform

    Returns:
        result (str): The lower cased, reversed string
    """
    return data.lower()[::-1]


def main():
    """
    Use the paths to an expected set of training data and the user-defined
    reverse function to reverse the training data contents.

    Note: This is the training entrypoint used by baklava!
    """

    # Read in the training data
    path = paths.input('training', 'train.txt')
    with open(path, 'r') as stream:
        content = stream.read()

    # Process the string training data
    result = process(content)

    # Write results back
    path = paths.model('model.txt')
    with open(path, 'w') as stream:
        stream.write(result)

    print('Success!')


if __name__ == '__main__':
    print(process('dlRow OlLeh'))
