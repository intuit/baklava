TensorFlow MNIST
================

This is an example job for training and deploying a `tensorflow` model
using `baklava`. This is similar to the previous examples but
downloads the training data to a temporary directory within the image
rather than loading it from an external directory.

Usage
-----

1. Install the release version of setuptools docker according to the
    directions found [Here](https://github.com/intuit/baklava)

2. Clone the repository and go to the `examples/` directory:

    ```
    git clone git@github.com:data-science/baklava.git
    cd baklava/examples/4-tensorflow-mnist
    ```

3. Build and execute the example training image using:

    ```
    python setup.py train -t train-image
    ```
    ```
    docker run                                           \
    -v $(pwd)/data/model/:/opt/ml/model/                 \
    train-image
    ```

    This will generate a TensorFlow checkpoint artifacts in the
    `data/model/` folder.

4. Build and execute the example prediction image using:

    ```
    python setup.py predict -t predict-image
    ```
    ```
    docker run                                           \
    -p 8080:8080                                         \
    -v $(pwd)/data/model/:/opt/ml/model/                 \
    predict-image
    ```

    This will host the prediction function on your local machine
    identically to how it would be hosted in sagemaker.

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
    --data '{}'                                 \
    http://localhost:8080/invocations
    ```

    Note: For simplicity a default input is used. A list of 784
    pixel intensities can be passed in to a `{"data": [...]}` payload
    for more testing.

    If everything was successful, the server should emit this JSON
    response:

    ```
    {"prediction": 5}
    ```
