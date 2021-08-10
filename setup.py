from setuptools import setup, find_packages


setup(
    name='mlbaklava',
    use_scm_version={
        'write_to': 'mlbaklava/__version.py',
        'write_to_template': '__version__ = \'{version}\''
    },
    maintainer='Intuit ML Platform',
    maintainer_email='baklava-maintainers@intuit.com',
    url='https://github.com/intuit/baklava',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=[
        'setuptools_scm',
    ],
    install_requires=[
        'docker>=2.0.0',   # Earliest with compatible `docker.from_env` API
        'appdirs>=1.4.0',  # First version compatible with current pip paths
        'six>=1.16.0'
    ],
    entry_points={
        'distutils.commands': [
            'process = mlbaklava.commands:Process',
            'train = mlbaklava.commands:Train',
            'batch = mlbaklava.commands:Batch',
            'deploy = mlbaklava.commands:Deploy',
        ],
        'distutils.setup_keywords': [
            'python_version = mlbaklava.commands:passthrough',
            'dockerlines = mlbaklava.commands:passthrough',
        ],
    }
)
