# flasktemplate-nodbbackend

A template for a bare minimum Flask API - no database backend. An endpoint 'sums' is added as an example:  
https://en.wikipedia.org/wiki/Summation  
Unit Tests use the unittest library.  

# Development Guidelines #

If using a Python IDE (Visual Studio Code, PyCharm, etc) it will try to detect the Python interpreter. The instructions below can be applied directly from the command line, without an IDE.    

*Note: this project was tested with Python >= 3.10.*  

## Local dependencies ##

You must have Docker locally installed. And also, install the following system dependencies:

Mac OS:  
*\# source system-macos-dependencies.sh*

Ubuntu 20.04 (Jammy):  
*\# source system-ubuntu20-dependencies.sh*

CentOS 7:  
*\# source system-centos7-dependencies.sh*

*Note: this project has been extensively tested only with Ubuntu 20.04.*  

Run the commands:

*$ python3 -m venv .venv*

*$ source .venv/bin/activate*

*$ pip install -r requirements.txt*

## Building ##

N/A

## Running unit tests ##

*$ export CONFIGENV=api.config.TestingConfig; coverage run -m unittest discover*

## Code coverage ##

*$ coverage report -m --omit=".venv/\*,tests/\*"*    

*$ coverage html --omit=".venv/\*,tests/\*"*  

## Running Code Quality checking ##

*$ pylint api/\*.py tests/\*.py*  

## (Development) Running the RESTful API (Backend) ##

In your IDE or terminal:

*$ export CONFIGENV=api.config.TestingConfig; python -m api.app*

RestFUL API endpoints:  

http://127.0.0.1:5000/  

or using Docker:

*\# docker build --tag api:develop .*

*\# docker run --rm -it --name api -p 8080:8080 -e CONFIGENV=api.config.TestingConfig api:develop*

RestFUL API endpoints:  

http://127.0.0.1:8080/  

## (Production) Running the RESTful API (Backend) ##

*\# docker build --tag api:latest .*  

*\# docker run --rm -it --name api -p 8080:8080 -e CONFIGENV=api.config.ProdConfig api:latest*  

RestFUL API endpoints:    

http://127.0.0.1:8080/  
