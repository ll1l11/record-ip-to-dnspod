#!/usr/bin/env python
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()


setup(
    name='record-ip-to-dnspod',
    version='0.1.1',
    description='Record IP Via DNSPod API.',
    long_description=readme,
    author='codeif',
    author_email='me@codeif.com',
    url='https://github.com/codeif/record-ip-to-dnspod',
    license='MIT',
    entry_points={
        'console_scripts': [
            'record-ip-to-dnspod = record_ip_to_dnspod.bin:main',
        ],
    },
    packages=find_packages(exclude=("tests", "tests.*")),
)
