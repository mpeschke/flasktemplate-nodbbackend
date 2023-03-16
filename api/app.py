# coding=UTF-8
"""
Module: Flask API interface, with routes to a RESTful model (HTTP methods).
"""
from flask import jsonify, request, Response, json
from api.validations import valid_sum_for_post
from api.settings import APP


SUMHELPSTRING = "Use a json format:" \
                "{'a1': 'the first addend'" \
                ", 'a2': 'the second addend'}. 'a1', 'a2' are mandatory. 'a1'" \
                ", 'a2' are numbers. Example: {'a1': 16, 'a2': 4} " \
                "200 OK, message body: {'a1': 16, 'a2': 4, 's': 20}"
SUMMALFORMEDDOCUMENT = "Malformed Sum document '{}'"


@APP.route('/', methods=['GET'])
def get_endpoints():
    """
    Return all endpoints supported by this microservice.
    """
    sums_request_base_url = request.base_url
    return jsonify(
        {
            'sums': f'{sums_request_base_url}sums'
        }
    )


# SUMS ######################################################################

@APP.route('/sums', methods=['GET'])
@APP.route('/sums/page/<int:page>', methods=['GET'])
def get_sums():
    """
    HTTP GET method for Sum objects
    :return: An empty dictionary. This template does not persist data, as it
    does not provide a database backend.
    """
    return jsonify({'sums': []})


@APP.route('/sums', methods=['POST'])
def post_sum():
    """
    HTTP POST method for Sum object
    :return: A JSON response with 'cp' added to the message body as the sum
    of 's1' and 's2' (200 HTTP code).
    This template does not persist data, as it does not provide a database
    backend.
    """
    request_data = request.get_json(force=True)
    status = 200
    if valid_sum_for_post(request_data):
        try:
            body = json.dumps(
                    {
                        'a1': request_data['a1'],
                        'a2': request_data['a2'],
                        's': int(request_data['a1']) + int(request_data['a2'])
                    }
                )
        except Exception as exc:
            body = json.dumps(
                {
                    "error": str(type(exc)),
                    "helpString": SUMHELPSTRING
                }
            )
            status = 400
    else:
        body = json.dumps({
            "error": SUMMALFORMEDDOCUMENT.format(request_data),
            "helpString": SUMHELPSTRING
        })
        status = 400

    return Response(body, status, mimetype="application/json")


def main():
    """
    Application entrypoint
    :return: int ErrorCode or 0 (Success)
    """
    APP.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
