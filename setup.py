#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


PROJECT_NAME = os.path.basename(os.path.abspath(os.curdir))

PROD_PACKAGES = [
    'boto3',
    'docker-compose',
    'lovely-pytest-docker<=0.0.5',
    'pytest>=3.5.0',
    'urllib3<1.25,>=1.21.1', # Throttled by requests 2.20.1 from docker-compose (conflict with botocore>=1.12.164)
]

DEV_PACKAGES = [
    'pylint',
    'sphinx_rtd_theme',
    'twine',
    'Sphinx',
]

PACKAGES = list(PROD_PACKAGES)
if (os.environ.get('APP_ENV') is not None and
        'dev' in os.environ.get('APP_ENV')):
    PACKAGES += DEV_PACKAGES


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-dynamodb2',
    version='0.1.0',
    author='Lou Markovski',
    author_email='lou.markovski@gmail.com',
    maintainer='Lou Markovski',
    maintainer_email='lou.markovski@gmail.com',
    license='MIT',
    url='https://github.com/loum/pytest-dynamodb2',
    description='A simple plugin to use with pytest',
    long_description=read('README.rst'),
    py_modules=['pytest_dynamodb2'],
    python_requires='>=3.6',
    install_requires=PACKAGES,
    packages=find_packages() + ['pytest_dynamodb2'],
    package_data={'pytest_dynamodb2/docker': ['*.yml']},
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'dynamodb2 = pytest_dynamodb2',
        ],
    },
)
