# coding=UTF-8
"""
Test Module: Test suites for the exceptions.py module.
"""
import unittest
from api.exceptions import ExceptionAPIResourceNotFound


class TestExceptions(unittest.TestCase):
    """
    Test Case suite: test Exception's 'message' property.
    """
    def test_exceptionapiresourcenotfound_message(self):
        """
        Test default constructor values.
        :return: None
        """
        message = "This is a message"
        try:
            raise ExceptionAPIResourceNotFound(message)
        except ExceptionAPIResourceNotFound as exc:
            self.assertEqual(exc.message, message)


if __name__ == '__main__':
    unittest.main()
