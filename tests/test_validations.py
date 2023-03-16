# coding=UTF-8
"""
Test Module: Test suites for the validations.py module.
"""
import unittest
from api.validations import valid_sum_for_post
from tests.utils import NEWSUM

ASSERTVALIDMESSAGE = "This Sum's dict object should be valid"
ASSERTINVALIDMESSAGE = "This Sum's dict object should NOT be valid"


class TestValidations(unittest.TestCase):
    """
    Test Case suite: test validations.py valid_pino function.
    """
    def test_valid_movie_for_post(self):
        """
        Test a valid Sum object (happy path).
        :return: None
        """
        self.assertTrue(valid_sum_for_post(NEWSUM),
                        ASSERTVALIDMESSAGE)

    def test_valid_movie_for_post_different_dict_order(self):
        """
        Test a valid Sum object (happy path). The order of the dictionary
        does not matter.
        :return: None
        """
        requestdata = {
            'a2': NEWSUM['a2'],
            'a1': NEWSUM['a1']
        }

        self.assertTrue(valid_sum_for_post(requestdata),
                        ASSERTVALIDMESSAGE)

    def test_invalid_missing_second_addend_set(self):
        """
        The Sum dict object is missing the mandatory 'a2'.
        :return: None
        """
        requestdata = {
            'a1': NEWSUM['a1']
        }

        self.assertFalse(valid_sum_for_post(requestdata),
                         ASSERTINVALIDMESSAGE)

    def test_invalid_missing_first_addend_set(self):
        """
        The Sum dict object is missing the mandatory 'a1'.
        :return: None
        """
        requestdata = {
            'a2': NEWSUM['a2']
        }

        self.assertFalse(valid_sum_for_post(requestdata),
                         ASSERTINVALIDMESSAGE)

    def test_invalid_missing_both_addends(self):
        """
        The Sum dict object is missing both mandatory 'a1' and 'a2'.
        :return: None
        """
        requestdata = {}

        self.assertFalse(valid_sum_for_post(requestdata),
                         ASSERTINVALIDMESSAGE)

    def test_invalid_extra_dict_items(self):
        """
        The Sum dict object has unexpected additional items.
        :return: None
        """
        requestdata = {
            'a1': NEWSUM['a1'],
            'a2': NEWSUM['a2'],
            'shouldnotbehere': 'whatever'
        }

        self.assertFalse(valid_sum_for_post(requestdata),
                         ASSERTINVALIDMESSAGE)

    def test_invalid_extra_dict_item(self):
        """
        The Sum dict object has unexpected (but valid) additional 's' item.
        :return: None
        """
        requestdata = {
            'a1': NEWSUM['a1'],
            'a2': NEWSUM['a2'],
            's': 100
        }

        self.assertFalse(valid_sum_for_post(requestdata),
                         ASSERTINVALIDMESSAGE)

    def test_invalid_request_object_type(self):
        """
        The request object is a string, not a dict.
        :return: None
        """
        requestdata = 'this is not a dictionary'

        self.assertFalse(valid_sum_for_post(requestdata),
                         ASSERTINVALIDMESSAGE)

    def test_invalid_request_object_none(self):
        """
        The request object is None, not a dict.
        :return: None
        """
        requestdata = None

        self.assertFalse(valid_sum_for_post(requestdata),
                         ASSERTINVALIDMESSAGE)
