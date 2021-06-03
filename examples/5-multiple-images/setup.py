from setuptools import setup, find_packages

setup(
    name='multiple_images',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'baklava.train': [
            'first = multiple_images.main:train1',
            'second = multiple_images.main:train1',
            'third = multiple_images.main:train2',
        ],
        'baklava.predict': [
            'third = multiple_images.main:predict1',
            'fourth = multiple_images.main:predict1',
            'fifth = multiple_images.main:predict2',
        ]
    }
)
