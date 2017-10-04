from setuptools import setup, find_packages
import pip

setup(
    name='pip-additions',
    author='Michael Distler',
    author='michael.distler@gmail.com',
    description='Additional Pip Utilities',
    packages=find_packages(),
    install_requires=[
        'setuptools'
    ],
    version=0.1
)

