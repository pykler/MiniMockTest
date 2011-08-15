from setuptools import setup, find_packages
import sys, os

setup(name='MiniMockTest',
      version='0.2',
      description="Custom unittest TestCase that wraps minimock",
      long_description="""\
Custom unittest TestCase that wraps minimock for easier use """,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='minimock mock mocking test unittest TestCase MockTestCase',
      author='Hatem Nassrat',
      author_email='hnassrat@gmail.com',
      url='http://pykler.github.com/MiniMockTest/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
