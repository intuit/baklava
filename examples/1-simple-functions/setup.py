from setuptools import setup, find_packages

setup(
    name='simple_functions',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'baklava.train': [
            'my_train = simple_functions.main:training_function',
        ],
        'baklava.predict': [
            'my_predict = simple_functions.main:hosted_function',
        ]
    }
)
