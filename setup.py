#!/usr/bin/env python
from setuptools import setup, find_packages

# Get some values from the setup.cfg
try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser
conf = ConfigParser()
conf.read(['setup.cfg'])
metadata = dict(conf.items('metadata'))

PACKAGENAME = metadata.get('package_name', 'packagename')
DESCRIPTION = metadata.get('description', 'package description')
AUTHOR = metadata.get('author', '')
LICENSE = metadata.get('license', 'unknown')
VERSION = '0.1.0.dev0'


setup(name=PACKAGENAME,
      version=VERSION,
      description=DESCRIPTION,
      install_requires=['pytest-runner'],
      tests_require=['pytest'],
      author=AUTHOR,
      license=LICENSE,
      packages=find_packages(),
)
