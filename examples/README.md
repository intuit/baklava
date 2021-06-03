Examples
========

Each of the subdirectories within this folder are a complete examples
of python projects that are compatible with SageMaker jobs and
deployment.

The examples showcase different use-cases:

1. [Simple Functions](1-simple-functions): The simplest possible package with a training and prediction job.
2. [SageMaker Paths](2-sagemaker-paths): Builds images that access standard SageMaker mounted paths. This allows models to be written to disk after training and models to be loaded from disk for prediction.
3. [Sklearn Tree](3-sklearn-tree): Creates a training and prediction image for a Scikit-Learn decision tree.
4. [Tensorflow MNIST](4-tensorflow-mnist): Creates a training and prediction image for in Tensorflow to predict the MNIST dataset.
5. [Multiple Images](5-multiple-images): Creates multiple training and prediction images from a single package.
6. [Internal Dependencies](6-internal-dependencies): Modifies the `Simple Functions` example to use an internal Intuit-specific package as a dependency.
7. [Custom Docker Lines](7-custom-doocker-lines): Modifies the `Simple Functions` example to inserts custom docker lines into the resulting dockerfile
8. [Predict Initializer](8-predict-initializer): Creates an initialization entrypoint for the predict image in order to load a model into memory as soon as the process starts.
9. [Non-Python Files](9-non-python-files): Creates a python distribution which correctly includes non-python files such as a `requirements.txt`
