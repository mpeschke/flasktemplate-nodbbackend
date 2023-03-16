# coding=UTF-8
"""
Test Module: Test suites for the config.py module.
"""
import unittest
from api.settings import APP


class TestConfig(unittest.TestCase):
    """
    Test Case suite: test TESTING configurations.
    """
    def test_config_exists(self):
        """
        Test APP.config setting has been instantiated.
        :return: None
        """
        self.assertFalse(isinstance(APP.config, type(None)),
                         'APP.config setting is missing!')

    def test_config_testing_set(self):
        """
        Test APP.config setting 'TESTING'.
        :return: None
        """
        self.assertTrue(APP.config['TESTING'],
                        'Config NOT set for TESTING run!')

    def test_config_testing_debug(self):
        """
        Test APP.config setting 'TESTING'.
        :return: None
        """
        self.assertTrue(APP.config['DEBUG'],
                        'Config NOT set for DEBUG!')

    def test_config_sums_per_page(self):
        """
        Test APP.config setting 'SUMS_PER_PAGE'.
        :return: None
        """
        self.assertFalse(isinstance(APP.config['SUMS_PER_PAGE'], type(None)),
                         'Sums per page (pagination) not set!')


if __name__ == '__main__':
    unittest.main()
