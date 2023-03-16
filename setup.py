# coding=UTF-8
# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='api',
    version='1.0.0',
    description='Flask backend template',
    long_description=readme,
    author='Matheus Peschke de Azevedo',
    author_email='mpeschke@gmail.com',
    url='https://github.com/mpeschke/flasktemplate-nodbbackend',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)