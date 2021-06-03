from setuptools import setup, find_packages

setup(
    name='logging_custom_response',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'baklava.initialize': [
            'init = logging_custom_response.main:load_model',
        ],
        'baklava.predict': [
            'pred = logging_custom_response.main:hosted_function',
        ]
    }
)
