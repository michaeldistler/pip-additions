from setuptools import setup, find_packages
import pip

setup(
    name='pip-additions',
    author='Michael Distler',
    author_email='michael.distler@gmail.com',
    description='Additional Pip Utilities',
    url='https://github.com/michaeldistler/pip-additions',
    download_url='https://github.com/michaeldistler/pip-additions/archive/0.1.tar.gz',
    packages=find_packages(),
    install_requires=[
        'setuptools'
    ],
    version=0.1
)

