Simple Functions
================

This is the a simple example package which can be used to build
SageMaker-compatible training and prediction images. These are intended
to be the **simplest** possible images.

Note that this example defines two entrypoints to create images for.
It is not necessary to define both training and prediction images for
your own package.

Usage
-----

1. Install the release version of setuptools docker according to the
    directions found [Here](https://github.com/intuit/baklava)

2. Clone the repository and go to the `examples/` directory:

    ```
    git clone git@github.com:data-science/baklava.git
    cd baklava/examples/1-simple-functions
    ```

3. Build and execute the example training image using:

    ```
    python setup.py train -t train-image
    ```

    This builds the image and tags it with the `train-image` identifier. 
    Passing this identifier to the `docker run` command will execute the image.

    ```
    docker run train-image
    ```

4. Build and execute the example prediction image using:

    ```
    python setup.py predict -t predict-image
    ```

    This builds the image and tags it with the `predict-image` identifier. 
    Passing this identifier to the `docker run` command will execute the image.

    ```
    docker run -p 8080:8080 predict-image
    ```

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
    --data '{"hello": "world"}'                 \
    http://localhost:8080/invocations
    ```

    If everything was successful, the server should emit this JSON
    response:

    ```
    {"hello": "world"}
    ```
