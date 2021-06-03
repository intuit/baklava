Predict Initializer
===================

This is an example which shows how to set up a predict so that it loads
the model artifact into memory as soon as the docker image is run. This
is important if the time it takes to run load model is long. If the
model takes a significant amount of time to load into memory, all calls
to `invocations` endpoint will hang while waiting for the model
artifact to load.

Setting up an initializer requires that another entrypoint is added to
the `setup.py` file. It should look like the following:

```
setup(
    ...
    entry_points={
        ...
        'baklava.initialize': [
            'init = simple_functions.main:load_model',
        ],
        ...
    }

    ...
)
```

This tells `baklava` to run the `load_model` method as soon
as the process has been started.

In this example the actual "model" just adds one to each of the values
within the JSON payload. An artificial latency is added to the
`load_model` method to simulate a model that takes a significant amount
of time to load into memory.

Usage
-----

1. Install the release version of setuptools docker according to the
    directions found [Here](https://github.com/intuit/baklava)

2. Clone the repository and go to the `examples/` directory:

    ```
    git clone git@github.com:data-science/baklava.git
    cd baklava/examples/8-predict-initializer
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

    This will host the prediction function on your local machine
    identically to how it would be hosted in sagemaker.

    Every time a new process is created, you should see the following
    output:

    ```
    Running Slow Load Function!
    ```

    This indicates that the initialization function has been run and
    that the result has been cached in memory. Due to the
    `functools.lru_cache` decorator, this message should only appear
    once per process. Every subsequent call to `load_model` will use
    the cached result.

4. The status of whether or not the server is running can be tested by
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

5. The prediction function defined in the `setup.py` can be run by
   accessing the `invocations` route. In another terminal, execute
   a `POST` request to the `invocations` route using `curl`:

    ```
    curl                                        \
    --header "Content-Type: application/json"   \
    --request POST                              \
    --data '{"a": 9, "b": 0}'                   \
    http://localhost:8080/invocations
    ```

    If everything was successful, the server should emit this JSON
    response:

    ```
    {"a": 10, "b": 1}
    ```
