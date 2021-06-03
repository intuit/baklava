Non-Python Files
================

This example builds upon the Sklearn tree example but includes
non-python files to perform the distribution setup and model evaluation.
By default `setuptools` **does not** include non-python files in
resulting distributions. Without explicit configuration this is an
issue if using a `requirements.txt` or configuration JSON files within
the package.

This example shows how non-python files are commonly used in a package
and then includes a `MANIFEST.in` to show how to make sure that these
are correctly packaged into your final package.

Here is a list of files which are included in the `MANIFEST.in`:

* `requirements.txt`: This is used by the setup script to install
    the package requirements. Using a requirements file is common
    practice since it allows you to capture every package being used
    in your current envionrment by running the command:
    `pip freeze > requirements.txt`.
* `dockerlines.txt`: Rather than including extra docker lines inline
    within the setup script, any lines that must run in docker prior
    to installing the package can be specified in this external file.
* `non_python_files/resources/thresholds.json`: This configuration file
    is loaded into python using package resource utilities. The
    thresholds are used to determine whether a good prediction can
    be made.

Note that these files are necessary for the package to work correctly
but would normally not get included into the distribution unless it is
explicitly included in the `MANIFEST.in` file.

Usage
-----

1. Install the release version of setuptools docker according to the
    directions found [Here](https://github.com/intuit/baklava)

2. Clone the repository and go to the `examples/` directory:

    ```
    git clone git@github.com:data-science/baklava.git
    cd baklava/examples/9-non-python-files
    ```

3. Build and execute the example training image using:

    ```
    python setup.py train -t train-image
    ```
    ```
    docker run                                           \
    -v $(pwd)/data/train/:/opt/ml/input/data/training/   \
    -v $(pwd)/data/model/:/opt/ml/model/                 \
    train-image
    ```

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
    --data '{"age": 35, "height": 182}'         \
    http://localhost:8080/invocations
    ```

    If everything was successful, the server should emit this JSON
    response:

    ```
    {"weight": 172}
    ```
