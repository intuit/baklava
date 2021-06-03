Logging And Custom Response
===========================

This example shows how to use the `baklava` provided logger as well as
using a tuple response in order to provide a custom status code. The rules 
behind how flask handles responses can be found 
[here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#about-responses).

To be able to use the augmented logging in a `baklava` project all
that is required is:

```python
import logging
logger = logging.getLogger("baklava")
```

This logger is only preconfigured in a prediction container. It is recommended 
to configure your own logger in a training container.

Usage
-----

1. Install the release version of setuptools docker according to the
    directions found [Here](https://github.com/intuit/baklava)

2. Clone the repository and go to the `examples/` directory:

    ```
    git clone git@github.com:data-science/baklava.git
    cd baklava/examples/10-logging-and-custom-responses
    ```

3. Build and execute the example prediction image using:

    ```
    python setup.py predict -t predict-image
    docker run -p 8080:8080 predict-image
    ```
   
   As soon as the second line is run, the server logs show be visible from
   stdout. Notice that the initialization function is logged once per process
   however the `tid` is blank. This is due to the fact that the initialization
   is not bound to an individual user.

4. Execute a `GET` request to the `ping` route using `curl`:

    ```
    curl http://localhost:8080/ping
    ```

    Expected Response:

    ```json
    {"success": true}
    ```

6. Execute a `POST` request to the `invocations` route using `curl`:

    ```
    curl                                                                                \
    --header "Content-Type: application/json"                                           \
    --header "X-Amzn-SageMaker-Custom-Attributes: 3853de45-7730-4674-9aa7-f79f0875cbd8" \
    --request POST                                                                      \
    --data '{"hello": "world"}'                                                         \
    http://localhost:8080/invocations
    ```

    Expected Response:

    ```text
    "OK"
    ```
   
    On the server side, you should now see that the TID provided in the 
    SageMaker custom attributes header is parsed and logged from both the
    nginx layer and the application code. This is because the logger specified
    by `'baklava'` includes the header by default.
