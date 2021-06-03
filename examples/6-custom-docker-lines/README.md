Custom Docker Lines
===================

This example project inserts custom docker commands into the image build
process to echo `"hello world"` at build time. This allows any
arbitrary docker commands can be executed directly in the image.

The difference between this example and the `1-simple-functions` example
is only visible within the `setup.py`

The following lines are added to the `setup` function:

```
from setuptools import setup, find_packages

setup(
    ...
    python_version='3.6',
    dockerlines="RUN echo hello world",
    ...
)
```

The `python_version` command allows you to specify which version of
python to build the image for. This requires that there is a
corresponding `python:slim` image available for the selected version.
By default, the dockerfile will use your environment's python version.

The `dockerlines` command will add the docker commands to the dockerfile
prior to installing the distribution and its requirements. This means
that if a python library has system dependencies, this can be installed
before the python library is installed.

Usage
-----

1. Install the release version of setuptools docker according to the
    directions found [Here](https://github.com/intuit/baklava)

2. Clone the repository and go to the `examples/` directory:

    ```
    git clone git@github.com:data-science/baklava.git
    cd baklava/examples/7-custom-docker-lines
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
