from setuptools import setup, find_packages

setup(
    name='sklearn_tree',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'sklearn',
        'pandas',
        'scipy',
    ],
    dockerlines=[
        'COPY /mlctlsriracha-0.0.11.tar.gz /opt/mlctlsriracha-0.0.11.tar.gz',
        'RUN pip install /opt/mlctlsriracha-0.0.11.tar.gz'
    ],
    python_version='3.6',
    entry_points={
        'baklava.train': [
            'my_training_entrypoint = sklearn_tree.train:main',
        ],
        'baklava.predict': [
            'my_prediction_entrypoint = sklearn_tree.predict:main',
        ]
    }
)
