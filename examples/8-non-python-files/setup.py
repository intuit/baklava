from setuptools import setup, find_packages


def lines(filename):
    """
    Read each line of a file into a list

    Args:
        filename (str): The name of the file to read
    Returns:
        lines (list[str]): The lines within the file
    """
    with open(filename) as stream:
        return stream.read().splitlines()


def requirements():
    return lines('requirements.txt')


def dockerlines():
    return lines('dockerlines.txt')


setup(
    name='non_python_files',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,

    # Specify requirements using text file
    install_requires=requirements(),

    # Specify baklava information
    python_version='2.7.15',
    dockerlines=dockerlines(),
    entry_points={
        'baklava.train': [
            'train = non_python_files.train:main',
        ],
        'baklava.initialize': [
            'init = non_python_files.predict:load_model',
        ],
        'baklava.predict': [
            'pred = non_python_files.predict:main',
        ]
    }
)
