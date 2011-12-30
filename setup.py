from distutils.core import setup
from setuptools import find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def find_packages_in(where, **kwargs):
    return [where] + ['%s.%s' % (where, package) for package in find_packages(where=where, **kwargs)]

setup(
    name = 'django-argparse-command',
    version = '0.1.0',
    author = 'Allan Lei',
    author_email = 'allanlei@helveticode.com',
    description = 'Django Commands using ArgumentParser',
    long_description=open('README.txt').read(),
    license='LICENSE.txt',
    keywords = 'django argparse commands optparse',
    url = 'https://github.com/allanlei/django-argparse-command',
    packages=find_packages_in('argcmd'),
    install_requires=[
    ],
)
