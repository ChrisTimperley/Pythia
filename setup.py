#!/usr/bin/python3
from setuptools import setup

setup(
    name='pythia',
    version='0.0.1',
    description='A test harness generation and handling solution',
    long_description='TBA',
    author='Chris Timperley',
    author_email='christimperley@googlemail.com',
    url='https://github.com/ChrisTimperley/Pythia',
    license='mit',
    packages=['pythia'],
    entry_points = {
        'console_scripts': [ 'pythia = pythia.pythia:main' ]
    }
)
