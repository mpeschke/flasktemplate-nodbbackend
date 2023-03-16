# coding=UTF-8
"""
Module: Environments config file.
https://pythonise.com/series/learning-flask/flask-configuration-files
https://flask.palletsprojects.com/en/1.1.x/config/
"""


class Config:
    """
    Base class for environment configuration
    """
    DEBUG = False
    TESTING = False
    SUMS_PER_PAGE = 5


class TestingConfig(Config):
    """
    Derived Class: TESTING ENVIRONMENT
    """
    DEBUG = True
    TESTING = True


class ProdConfig(Config):
    """
    Derived Class: PRODUCTION ENVIRONMENT
    """
    DEBUG = False
    TESTING = False
