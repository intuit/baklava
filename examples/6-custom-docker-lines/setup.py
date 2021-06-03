from setuptools import setup, find_packages

setup(
    name='custom_docker_lines',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    python_version='3.6',
    dockerlines="RUN echo hello world",
    entry_points={
        'baklava.train': [
            'my_train = simple_functions.main:training_function',
        ],
        'baklava.predict': [
            'my_predict = simple_functions.main:hosted_function',
        ]
    }
)
