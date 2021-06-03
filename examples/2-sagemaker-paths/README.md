SageMaker Paths
===============
For the actual functionality of the package, an example "model" is used.
The artifact that is produced during "training" is a string
`"hello world"`. The "prediction" that is computed using the model
artifact is a concatenation of the input data and the `"hello world"`
string.

This is a simple example package which can be used to build
SageMaker-compatible training and prediction images. This package
defines images which access standard mount paths that the SageMaker
service automatically adds to each image. These paths are populated with
data from S3 or written back to S3 depending on the configuration. This
allows models for a number of necessary features:

1. Training data can be loaded from disk at training time
2. Models can be written to disk after training
3. Models can be loaded from disk for prediction

The following usage documentation shows you how to perform these S3
path operations completely locally by mounting data in the same way
that SageMaker mounts data to your images.

Usage
-----

1. Install the release version of setuptools docker according to the
    directions found [Here](https://github.com/intuit/baklava)

2. Clone the repository and go to the `examples/` directory:

    ```
    git clone git@github.com:data-science/baklava.git
    cd baklava/examples/2-sagemaker-paths
    ```

3. Build and execute the example training image using:

    ```
    python setup.py train -t train-image
    ```

    This builds the image and tags it with the `train-image` identifier. 
    Passing this identifier to the `docker run` command will execute the image.
    In addition to telling it what image to use, we also mount local directories 
    to predefined SageMaker paths.

    ```
    docker run                                           \
    -v $(pwd)/data/train/:/opt/ml/input/data/training/   \
    -v $(pwd)/data/model/:/opt/ml/model/                 \
    train-image
    ```

    This will generate a `model.txt` file in the `data/model/` folder.

4. Build and execute the example prediction image using:

    ```
    python setup.py predict -t predict-image
    ```

    This builds the image and tags it with the `predict-image` identifier. 
    Passing this identifier to the `docker run` command will execute the image.
    In addition to telling it what image to use, we also mount local directories 
    to predefined SageMaker paths.

    ```
    docker run                                           \
    -p 8080:8080                                         \
    -v $(pwd)/data/model/:/opt/ml/model/                 \
    predict-image
    ```

    This will host the prediction function on your local machine
    identically to how it would be hosted in SageMaker.

5. The status of whether or not the server is running can be tested by
   accessing the `ping` route. In another terminal, execute a `GET` request
   to the `ping` route using `curl`:

    ```
    curl                                        \
    --header "Content-Type: application/json"   \
    --request GET                               \
    http://localhost:8080/ping
    ```

    If everything was successful, the server should emit this JSON
    response:

    ```
    {"success": true}
    ```

6. The prediction function defined in the `setup.py` can be run by
   accessing the `invocations` route. In another terminal, execute
   a `POST` request to the `invocations` route using `curl`:

    ```
    curl                                        \
    --header "Content-Type: application/json"   \
    --request POST                              \
    --data '{"data": "sailor "}'                \
    http://localhost:8080/invocations
    ```

    If everything was successful, the server should emit this JSON
    response:

    ```
    {"data": "sailor hello world"}
    ```
