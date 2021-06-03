Multiple Images
===============

There may be times when multiple models are hosted within a single
repository. This can mean that a repository contains multiple training
functions for distinct models or multiple hosting functions. In this
case `baklava` provides functionality to build images for a
selected entrypoint among multiple.

Usage
-----

1. Install the release version of setuptools docker according to the
    directions found [Here](https://github.com/intuit/baklava)

2. Clone the repository and go to the `examples/` directory:

    ```
    git clone git@github.com:data-science/baklava.git
    cd baklava/examples/5-multiple-images
    ```

3. Build and execute each of the distinct training images using:

    ```
    python setup.py train --entrypoint first -t first-train
    docker run first-train
    python setup.py train --entrypoint second -t second-train
    docker run second-train
    python setup.py train --entrypoint third -t third-train
    docker run third-train
    ```

4. Build and execute each of the distinct prediction images using:

    ```
    python setup.py predict --entrypoint third -t third-predict
    python setup.py predict --entrypoint fourth -t fourth-predict
    python setup.py predict --entrypoint fifth -t fifth-predict
    ```

    Execute one of the the prediction images:

    ```
    docker run -p 8080:8080 fifth-predict
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
    --data '{"hello": "world"}'                \
    http://localhost:8080/invocations
    ```

    If everything was successful, the server should emit this JSON
    response:

    ```
    {"hello": "world"}
    ```
