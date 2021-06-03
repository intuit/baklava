from setuptools import setup, find_packages

setup(
    name='sagemaker_paths',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'baklava.train': [
            'train = sagemaker_paths.train:main',
        ],
        'baklava.predict': [
            'predict = sagemaker_paths.predict:main',
        ]
    }
)
