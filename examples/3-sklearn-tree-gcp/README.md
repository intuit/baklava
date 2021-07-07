Sklearn Tree
============

This is an example project which builds on the first two examples but
builds a real model using the `sklearn` package. The major difference
between the first two examples and this one is that this includes many
more dependencies in the `setup.py`

Usage
-----

1. Install the release version of setuptools docker according to the
    directions found [Here](https://github.com/intuit/baklava)

2. Clone the repository and go to the `examples/` directory:

    ```
    git clone git@github.com:data-science/baklava.git
    cd baklava/examples/3-sklearn-tree
    ```

3. Build and execute the example training image using:

    ```
    python setup.py train -t train-image
    ```
    ```
    docker run \
    -it --entrypoint=/bin/bash \
    -v ~/gcp_creds.json/:/etc/gcp_creds.json \
    -e GOOGLE_APPLICATION_CREDENTIALS=/etc/gcp_creds.json \
    -e AIP_TRAINING_DATA_URI=mlctl-data \
    -e AIP_MODEL_DIR=mlctl-train \
    train-image
    ```

        docker run \
    -it entrypoint=/bin/bash
    -v ~/gcp_creds.json/:/etc/gcp_creds.json \
    -e GOOGLE_APPLICATION_CREDENTIALS=/etc/gcp_creds.json \
    -e AIP_TRAINING_DATA_URI=mlctl-data \
    -e AIP_MODEL_DIR=mlctl-train \
    -e FUNCTION_REGION=us-central1 \
    train-image

    This will generate a `model.pkl` file in the `data/model/` folder.

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
    --data '{"instances":[{"age": 35, "height": 182}]}'         \
    http://localhost:8080/invocations
    ```

    If everything was successful, the server should emit this JSON
    response:

    ```
    {"weight": 172}
    ```
