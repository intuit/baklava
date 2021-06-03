"""
Model
=====
Defines the model architecture used during training and prediction
"""
import tensorflow as tf


def build():
    """
    Builds a model graph which can be trained to compute MNIST predictions.

    Returns:
        graph (~tf.Graph): The tensorflow graph which contains all operations.
        x (~tf.Tensor): A placeholder which acts as the feature input
        y (~tf.Tensor): A placeholder which acts as the label input
        initializer (~tf.Tensor): A tensor which initializes all variables
        accuracy (~tf.Tensor): A tensor which computes the accuracy for the
            current input data. Requires that values are fed into both x and y.
        prediction (~tf.Tensor): A tensor which computes the predicted value
            for y.
    """

    graph = tf.Graph()
    with graph.as_default():

        # Define global inputs
        y = tf.placeholder(tf.float32, [None, 10])
        x = tf.placeholder(tf.float32, [None, 784])

        # Peform matrix multiplication
        logits = tf.layers.dense(x, 10)

        # Define your loss function
        cross_entropy = tf.nn.softmax_cross_entropy_with_logits_v2(
            labels=y,
            logits=logits
        )
        loss = tf.reduce_mean(cross_entropy)

        # Metrics
        correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        prediction = tf.squeeze(tf.argmax(logits, 1))

        # A single optimization step
        step = tf.train.GradientDescentOptimizer(0.5).minimize(loss)

        # Graph initialization
        initializer = tf.global_variables_initializer()

    return graph, x, y, step, initializer, accuracy, prediction
