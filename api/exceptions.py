# coding=UTF-8
"""
Module: Custom made exceptions.
"""


class ExceptionAPIResourceNotFound(Exception):
    """
    Exception to indicate a RESTful API resource was not found.
    """

    def __init__(self, message):
        """
        Constructor
        :param message: the exception message.
        """
        super().__init__(message)
        self.message = message
