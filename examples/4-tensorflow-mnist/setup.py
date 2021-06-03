from setuptools import setup, find_packages

setup(
    name='tensorflow_mnist',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'tensorflow',
    ],
    python_version='3.6',
    entry_points={
        'baklava.train': [
            'train = tensorflow_mnist.train:main',
        ],
        'baklava.predict': [
            'predict = tensorflow_mnist.predict:main',
        ]
    }
)
