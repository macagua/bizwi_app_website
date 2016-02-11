import requests
from settings import URL_API_V1
import json


"""
 Definition Functions basic
"""


def base_request_no_json(url_path):
    """
        Do a GET to the REST API and return a JSON with the requests response
    """
    response = requests.get(URL_API_V1 + url_path)
    if response.status_code != 200:  # if its a response like a 404
        return response  # do not json() it
    else:
        return response


def base_request(url_path):
    """
        Do a GET to the REST API and return a JSON with the requests response
    """
    response = requests.get(URL_API_V1 + url_path)
    if response.status_code != 200:  # if its a response like a 404
        return response  # do not json() it
    else:
        return response.json()


def base_post(url_path, content):
    """
        Do a POST to the REST API
    """
    response = requests.post(url=URL_API_V1 + url_path, json=content)
    return response
"""
End functions basics
"""


"""
Functions to management employees
"""


def get_employees(client, id_employee=None):
    url_path = 'employee_list/' + str(client)
    if id_employee:
        url_path += '/' + str(id_employee)
    result = base_request(url_path)
    return result
