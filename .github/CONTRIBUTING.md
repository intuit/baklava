# Contribution Guidelines

First of all, thank you for your interest in contributing to this project !

* Before submitting a [Pull Request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests) (PR), please make sure that you have had a discussion with the project-leads
* If a [relevant issue](https://github.com/intuit/baklava/issues) already exists, have a discussion within that issue (by commenting) - and make sure that the project-leads are okay with your approach
* If no relevant issue exists, please [open a new issue](https://github.com/intuit/baklava/issues) to start a discussion
* Please proceed with a PR only *after* the project admins or owners are okay with your approach. We don't want you to spend time and effort working on something - only to find out later that it was not aligned with how the project developers were thinking about it !
* You can refer to the [Developer Guide](https://github.com/intuit/karate/wiki/Developer-Guide) for information on how to build and test the project on your local / developer machine
* **IMPORTANT**: Submit your PR(s) against the [`develop`](https://github.com/intuit/baklava/tree/develop) branch of this repository

If you are interested in project road-map items that you can potentially contribute to, please refer to the [Project Board]().

## Development

1. Install docker from the following URL:

    ```
    https://www.docker.com/
    ```

2. (*Optional*) Create a new virtual environment for `baklava`

    ```
    pip install virtualenv
    virtualenv ~/envs/baklava
    source ~/envs/baklava/bin/activate
    ```

3. Clone and install the repository:

    ```
    git clone git@github.com:intuit/baklava.git
    pip install --editable baklava/
    ```

   This will install a version to an isolated environment in editable
   mode. As you update the code in the repository, the new code will
   immediately be available to run within the environment (without the
   need to `pip install` it again)

4. Run the tests using `tox`:

    ```
    pip install tox
    tox
    ```

   Tox will run all of the tests in isolated environments for both
   python 2.7 and python 3.6.

   **Note**: Tests will produce >40GB worth of images
