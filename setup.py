from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='baklava',
    long_description=long_description,
    long_description_content_type='text/markdown',
    use_scm_version={
        'local_scheme': 'no-local-version',
        'write_to': 'baklava/__version.py',
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
            'train = baklava.commands:Train',
            'execute = baklava.commands:Train',
            'predict = baklava.commands:Predict',
            'serve = baklava.commands:Predict',
        ],
        'distutils.setup_keywords': [
            'python_version = baklava.commands:passthrough',
            'dockerlines = baklava.commands:passthrough',
        ],
    }
)
