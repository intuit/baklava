"""
Train
=====
Defines functions which train models and write model artifacts to disk.
"""
from __future__ import print_function

import os
import tempfile

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

from tensorflow_mnist import model, paths


def train(path):
    """
    Train a decision tree classifier using a floating point feature matrix and
    a categorical classification target.

    Arguments:
        path (str): The path indicating where to save the final model artifacts
    """

    # Construct the model graph
    graph, x, y, step, initializer, accuracy, prediction = model.build()

    # Start a training session
    with tf.Session(graph=graph) as sess:

        # Initialize the graph
        sess.run(initializer)

        # Train the model for 1000 steps
        mnist = input_data.read_data_sets(tempfile.mkdtemp(), one_hot=True)
        for _ in range(1000):
            batch_xs, batch_ys = mnist.train.next_batch(100)
            sess.run(step, feed_dict={x: batch_xs, y: batch_ys})

        # Display accuracy measurement
        print(sess.run(accuracy, feed_dict={x: mnist.test.images,
                                            y: mnist.test.labels}))
        # Save the variable data to disk
        os.makedirs(path)
        saver = tf.train.Saver()
        saver.save(sess, path)

    print('Success!')


def main():
    """
    Load features and labels, train the neural network, and serialize model
    artifact.

    Note: This is the training entrypoint used by baklava!
    """
    path = paths.model('mnist')
    train(path)
