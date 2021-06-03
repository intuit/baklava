from setuptools import setup, find_packages

setup(
    name='predict_initializer',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'baklava.initialize': [
            'init = predict_initializer.main:load_model',
        ],
        'baklava.predict': [
            'pred = predict_initializer.main:predict',
        ]
    }
)
