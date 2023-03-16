# coding=UTF-8
"""
Test Module: Test suites for the app.py module.
"""
from tests.utils import TestAppClient, GENERICMALFORMEDDOC, NEWSUM, \
    NEWSUMPROCESSED, MIME_APPJSON, MIME_TEXTHTML, UNITTESTCHECK_TEXTHTML, \
    UNITTESTCHECK_APPJSON, UNITTESTCHECK_CODE200, UNITTESTCHECK_CODE400, \
    UNITTESTCHECK_CODE404, UNITTESTCHECK_ERRHELPSTR, UNITTESTCHECK_LOCNONE, \
    UNITTESTCHECK_ARRELEM, UNITTESTCHECK_RESPONSE
from api.app import SUMHELPSTRING, SUMMALFORMEDDOCUMENT


#
# FLASK ROUTE FRAMEWORK TESTING
# (Validates responses from Flask when supplying an invalid route)
#
class TestAppFlaskRoutesFramework(TestAppClient):
    """
    Test Case suite: validate Flask Route Framework.
    """
    def test_flask_get_nonexistent_route(self):
        """
        Test Flask response for non-existent HTTP GET routes
        """
        response = self.client.get('this route does not exist')
        self.assertEqual(response.status_code,
                         404,
                         UNITTESTCHECK_CODE404)
        self.assertEqual(response.mimetype,
                         MIME_TEXTHTML,
                         UNITTESTCHECK_TEXTHTML)
        self.assertEqual(response.location,
                         None,
                         UNITTESTCHECK_LOCNONE)

    def test_flask_post_nonexistent_route(self):
        """
        Test Flask response for non-existent HTTP POST routes
        """
        response = self.client.post('/PARALELEPIPEDO/XPTO')
        self.assertEqual(response.status_code,
                         404,
                         UNITTESTCHECK_CODE404)
        self.assertEqual(response.mimetype,
                         MIME_TEXTHTML,
                         UNITTESTCHECK_TEXTHTML)
        self.assertEqual(response.location,
                         None,
                         UNITTESTCHECK_LOCNONE)

    def test_flask_put_nonexistent_route(self):
        """
        Test Flask response for non-existent HTTP PUT routes
        """
        response = self.client.put('/PARALELEPIPEDO/XPTO')
        self.assertEqual(response.status_code,
                         404,
                         UNITTESTCHECK_CODE404)
        self.assertEqual(response.mimetype,
                         MIME_TEXTHTML,
                         UNITTESTCHECK_TEXTHTML)
        self.assertEqual(response.location,
                         None,
                         UNITTESTCHECK_LOCNONE)

    def test_flask_patch_nonexistent_route(self):
        """
        Test Flask response for non-existent HTTP PATCH routes
        """
        response = self.client.patch('/PARALELEPIPEDO/XPTO')
        self.assertEqual(response.status_code,
                         404,
                         UNITTESTCHECK_CODE404)
        self.assertEqual(response.mimetype,
                         MIME_TEXTHTML,
                         UNITTESTCHECK_TEXTHTML)
        self.assertEqual(response.location,
                         None,
                         UNITTESTCHECK_LOCNONE)

    def test_flask_delete_nonexistent_route(self):
        """
        Test Flask response for non-existent HTTP DELETE routes
        """
        response = self.client.delete('/PARALELEPIPEDO/XPTO')
        self.assertEqual(response.status_code,
                         404,
                         UNITTESTCHECK_CODE404)
        self.assertEqual(response.mimetype,
                         MIME_TEXTHTML,
                         UNITTESTCHECK_TEXTHTML)
        self.assertEqual(response.location,
                         None,
                         UNITTESTCHECK_LOCNONE)


#
# HTTP GET TESTS
#
class TestAppMovieGet(TestAppClient):
    """
    Test Case suite: HTTP GET scenarios.
    """
    def test_sums_get_all_sums(self):
        """
        This unit test validates that the current implementation returns no
        Sums.
        """
        response = self.client.get('/sums')
        self.assertEqual(response.status_code,
                         200,
                         UNITTESTCHECK_CODE200)
        self.assertEqual(response.mimetype,
                         MIME_APPJSON,
                         UNITTESTCHECK_APPJSON)
        self.assertEqual(response.json,
                         {'sums': []},
                         UNITTESTCHECK_ARRELEM)


#
# HTTP POST TESTS
#
class TestAppMoviePost(TestAppClient):
    """
    Test Case suite: HTTP POST scenarios.
    """
    def test_sums_post(self):
        """
        This unit test validates the API response of creating a Sum
        (Happy Path).
        """
        response = self.client.post('/sums', json=NEWSUM)
        self.assertEqual(response.status_code,
                         200,
                         UNITTESTCHECK_CODE200)
        self.assertEqual(response.mimetype,
                         MIME_APPJSON,
                         UNITTESTCHECK_APPJSON)
        self.assertEqual(response.json,
                         NEWSUMPROCESSED,
                         UNITTESTCHECK_RESPONSE.format(str(NEWSUMPROCESSED)))

    def test_sums_invalid_missing_second_addend_set(self):
        """
        This unit test validates the API response of calculating a Sum -
        but the second addend is missing.
        """
        json = {'a1': 0}
        response = self.client.post('/sums', json=json)
        self.assertEqual(response.status_code,
                         400,
                         UNITTESTCHECK_CODE400)
        self.assertEqual(response.mimetype,
                         MIME_APPJSON,
                         UNITTESTCHECK_APPJSON)
        self.assertEqual(response.json,
                         {'error': SUMMALFORMEDDOCUMENT.format(str(json)),
                          'helpString': SUMHELPSTRING},
                         UNITTESTCHECK_ERRHELPSTR)

    def test_sums_invalid_missing_first_addend_set(self):
        """
        This unit test validates the API response of calculating a Sum -
        but the first addend is missing.
        """
        json = {'a2': 0}
        response = self.client.post('/sums', json=json)
        self.assertEqual(response.status_code,
                         400,
                         UNITTESTCHECK_CODE400)
        self.assertEqual(response.mimetype,
                         MIME_APPJSON,
                         UNITTESTCHECK_APPJSON)
        self.assertEqual(response.json,
                         {'error': SUMMALFORMEDDOCUMENT.format(str(json)),
                          'helpString': SUMHELPSTRING},
                         UNITTESTCHECK_ERRHELPSTR)

    def test_sums_invalid_missing_both_addends(self):
        """
        This unit test validates the API response of calculating a Sum -
        but both first and second addends are missing.
        """
        json = {}
        response = self.client.post('/sums', json=json)
        self.assertEqual(response.status_code,
                         400,
                         UNITTESTCHECK_CODE400)
        self.assertEqual(response.mimetype,
                         MIME_APPJSON,
                         UNITTESTCHECK_APPJSON)
        self.assertEqual(response.json,
                         {'error': SUMMALFORMEDDOCUMENT.format(str(json)),
                          'helpString': SUMHELPSTRING},
                         UNITTESTCHECK_ERRHELPSTR)

    def test_sums_invalid_extra_dict_item(self):
        """
        This unit test validates the API response of calculating a Sum -
        but there's and additional, unexpected extra item in the request.
        """
        json = {'a1': 0, 'a2': 0, 's': 0}
        response = self.client.post('/sums', json=json)
        self.assertEqual(response.status_code,
                         400,
                         UNITTESTCHECK_CODE400)
        self.assertEqual(response.mimetype,
                         MIME_APPJSON,
                         UNITTESTCHECK_APPJSON)
        self.assertEqual(response.json,
                         {'error': SUMMALFORMEDDOCUMENT.format(str(json)),
                          'helpString': SUMHELPSTRING},
                         UNITTESTCHECK_ERRHELPSTR)

    def test_sums_invalid_first_addend_not_a_number(self):
        """
        This unit test validates the API response of calculating a Sum -
        but the first addend is not a number.
        """
        json = {'a1': 'NaN', 'a2': 0}
        response = self.client.post('/sums', json=json)
        self.assertEqual(response.status_code,
                         400,
                         UNITTESTCHECK_CODE400)
        self.assertEqual(response.mimetype,
                         MIME_APPJSON,
                         UNITTESTCHECK_APPJSON)
        self.assertEqual(response.json,
                         {'error': "<class 'ValueError'>",
                          'helpString': SUMHELPSTRING},
                         UNITTESTCHECK_ERRHELPSTR)

    def test_sums_invalid_second_addend_not_a_number(self):
        """
        This unit test validates the API response of calculating a Sum -
        but the second addend is not a number.
        """
        json = {'a1': 0, 'a2': 'NaN'}
        response = self.client.post('/sums', json=json)
        self.assertEqual(response.status_code,
                         400,
                         UNITTESTCHECK_CODE400)
        self.assertEqual(response.mimetype,
                         MIME_APPJSON,
                         UNITTESTCHECK_APPJSON)
        self.assertEqual(response.json,
                         {'error': "<class 'ValueError'>",
                          'helpString': SUMHELPSTRING},
                         UNITTESTCHECK_ERRHELPSTR)

    def test_movies_post_malformed_document(self):
        """
        This unit test validates the API response when the request json is
        malformed.
        """
        response = self.client.post('/sums',
                                    json=GENERICMALFORMEDDOC)
        self.assertEqual(response.status_code,
                         400,
                         UNITTESTCHECK_CODE400)
        self.assertEqual(response.mimetype,
                         MIME_APPJSON,
                         UNITTESTCHECK_APPJSON)
        self.assertEqual(response.json,
                         {'error': SUMMALFORMEDDOCUMENT.format(
                             GENERICMALFORMEDDOC),
                          'helpString': SUMHELPSTRING},
                         UNITTESTCHECK_ERRHELPSTR)
