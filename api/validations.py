# coding=UTF-8
"""
Module: HTTP request validations
"""
SUMPOST = {
    'a1': 0,
    'a2': 0
}


def valid_model(model, requestdata):
    """
    Validates a model representation as a Python dictionary.
    This template serves for the following scenario: ALL dict keys MUST be
    in the request data.
    :param requestdata: a python dictionary
    :param model: a python dictionary
    :return: True or False
    """
    valid = True

    if isinstance(requestdata, dict):
        for key in requestdata:
            if key not in model:
                valid = False
                break
    else:
        return False

    return valid and len(requestdata) == len(model)


def valid_sum_for_post(requestdata):
    """
    Validates movie as a correct dictionary
    :param requestdata: a python dictionary
    :return: True or False
    """
    return valid_model(SUMPOST, requestdata)
