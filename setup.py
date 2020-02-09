#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='asciimatics_slides',
      version='1.0',
      packages=find_packages(),
      license='Apache 2.0',
      install_requires=[
            'asciimatics >= 1.11.0'
      ]
)