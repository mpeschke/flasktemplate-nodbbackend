# coding=UTF-8
"""
Test Module: Test suites for the models.py module.
"""
import unittest
from api.app import APP

UNITTESTSUM = {
    'a1': 999,
    'a2': 1
}
GENERICMALFORMEDDOC = \
    {
        'DOESNOT': 'DOESNOT',
        'EXIST': 'EXIST'
    }
NEWSUM = \
    {
        'a1': 999,
        'a2': 1
    }
NEWSUMPROCESSED = \
    {
        'a1': 999,
        'a2': 1,
        's': 1000
    }
NONEXISTINGSUM = EXISTINGSUM = \
    {
        'a1': 999,
        'a2': 1
    }

TESTSERVER = 'http://localhost{}'
MIME_APPJSON = 'application/json'
MIME_TEXTHTML = 'text/html'

UNITTESTCHECK_TEXTHTML = 'Expected text/html as mime type.'
UNITTESTCHECK_APPJSON = 'Expected application/json as mime type.'
UNITTESTCHECK_CODE200 = 'Expected HTTP response code 200 OK.'
UNITTESTCHECK_CODE400 = 'Expected HTTP response code 400 MALFORMED DOCUMENT.'
UNITTESTCHECK_CODE404 = 'Expected HTTP response code 404 NOT FOUND.'
UNITTESTCHECK_CODE409 = 'Expected HTTP response code 409 CONFLICT.'
UNITTESTCHECK_CODE201 = 'Expected HTTP response code 201 CREATED.'
UNITTESTCHECK_CODE204 = 'Expected HTTP response code 204 NO CONTENT.'
UNITTESTCHECK_ERRHELPSTR = "Unexpected field/values 'error' and 'helpString'"
UNITTESTCHECK_LOCATION = "Unexpected location of the created/updated resourc' \
                         'e '{}'."
UNITTESTCHECK_LOCNONE = "Expected location to be 'None'"
UNITTESTCHECK_ARRELEM = 'Unexpected element(s) or number of elements in the ' \
                        'array.'
UNITTESTCHECK_RESPONSE = "Expected response is '{}'."


class TestAppClient(unittest.TestCase):
    """
    Test Case template:
    This superclass does NOT populate the test database and uses
    the APP instance to access the API.
    """
    @classmethod
    def setUpClass(cls):
        """
        Creates all database objects (tables) and defines a client to access
        the Flask webserver interface.
        Scope: before the first class instance initiates
        :return: None
        """
        cls.client = APP.test_client()

    def tearDown(self):
        """
        Deletes all records from the tables.
        Scope: after every test case is completed.
        :return: None
        """

    @classmethod
    def tearDownClass(cls):
        """
        Destroys all database tables.
        Scope: after the last class instance exits
        :return: None
        """
