# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='RaptorBot',
    version='0.0.0',
    description='RaptorBot',
    long_description=readme,
    author='Peter Esser',
    author_email='me@kennethreitz.com',
    url='https://github.com/3DExtended/RaptorBot',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
