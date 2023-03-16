# coding=UTF-8
"""
Module: Load Flask and other modules' configuration.
"""
import os
from flask import Flask

APP = Flask(__name__)
APP.config.from_object(os.environ.get("CONFIGENV", "config.TestingConfig"))
