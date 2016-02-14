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


def create_client_admin(info):
    url_path = 'create_client_admin/'
    result = base_post(url_path, info)
    try:
        if result.status_code == 201:
            return {'success': True}
        else:
            resp = json.loads(result.text)
            resp['success'] = False
            return resp
    except Exception as e:
        print e
        return {'success': False, 'error': 'undefined'}


def auth(username, password):
    url_path = 'auth/'
    content = {'username': username, 'password': password}
    result = base_post(url_path, content)
    return result


def get_info(employee_id):
    url_path = 'employee/' + str(employee_id)
    result = base_request(url_path)
    return result


# news
def get_info_client(client_id):
    url_path = 'client/' + str(client_id)
    result = base_request(url_path)
    return result


def get_info_user(user_id):
    url_path = 'user/' + str(user_id)
    result = base_request(url_path)
    return result


def save_info_user(user_id, content):
    url_path = 'user/' + str(user_id)
    result = base_post(url_path, content)
    return result.status_code == 204


def save_info(employee_id, content):
    url_path = 'employee/' + str(employee_id)
    result = base_post(url_path, content)
    return result.status_code == 204


# info about client
def save_info_client(client_id, content):
    url_path = 'client/' + str(client_id)
    result = base_post(url_path, content)
    return result.status_code == 204


def change_password(employee_id, new_password):
    url_path = 'employee/set_pass' + "/" + str(employee_id)
    result = base_post(url_path, {'pass': new_password})
    return result.status_code == 202


# New method to change password of user (custom User ) --> ( no clients, no employee )
def change_password_user(user_id, new_password):
    url_path = 'user/set_pass' + "/" + str(user_id)
    result = base_post(url_path, {'pass': new_password})
    return result.status_code == 202


def get_context(employee_id):
    url_path = 'get_employee_context/' + str(employee_id)
    result = base_request(url_path)
    return result


def get_sensors_positions(id_location):
    url_path = 'sensors/' + str(id_location)
    result = base_request(url_path)
    return result


def get_sensor_log(id_customer, sensor_id, date_format):
    url_path = 'sensor_log/' + str(id_customer) + '/' + str(sensor_id) + '/' + str(date_format)
    result = base_request(url_path)
    return result


def get_visitors(id_customer, id_location, filter=None):
    if filter:
        url_path = 'visitors_filtered/' + str(id_customer) + '/' + str(id_location) + '?' + filter
    else:
        url_path = 'visitors/' + str(id_customer) + '/' + str(id_location)
    result = base_request(url_path)
    return result


def get_visitors_filtered_by_promotion(id_customer, id_location, id_promotion):
    url_path = 'visitors_filtered_by_promotion/' + str(id_customer) + '/' + str(id_location) + '/' + str(id_promotion)
    result = base_request(url_path)
    return result


def get_all_visitors(id_location):
    url_path = 'visitors_all/' + str(id_location)
    result = base_request(url_path)
    return result


def get_user_info(id_client, id_customer):
    url_path = 'client/' + str(id_client) + '/' + str(id_customer)
    result = base_request(url_path)
    return result


def get_pedestrians_stats(id_location, year, month=None, day=None, year2=None, month2=None, day2=None):
    url_path = 'pedestrians_stats/' + str(id_location) + '/' + str(year)
    if month:
        url_path += '/' + str(month)
    if day:
        url_path += '/' + str(day) + '/' + str(year2) + '/' + str(month2) + '/' + str(day2)
    result = base_request(url_path)
    return result


def get_stats(id_location):
    url_path = 'metrics/' + str(id_location)
    result = base_request(url_path)
    return result


def get_today_birthdays(id_location):
    url_path = 'birthdays/' + str(id_location)
    result = base_request(url_path)
    return result


def get_promotion_requests(id_customer):
    url_path = 'promotion_requests/' + str(id_customer)
    result = base_request(url_path)
    return result


def get_ext_promotion_location(id_ext_promotion_location):
    url_path = 'external_promotion_location/' + id_ext_promotion_location
    result = base_request(url_path)
    return result


def get_next_birthdays(id_location):
    url_path = 'next_birthdays/' + str(id_location)
    result = base_request(url_path)
    return result


def get_messages(id_customer, id=None, limit=None):
    url_path = 'message_to_customer/' + str(id_customer)
    if id:
        url_path += '/' + id
    elif limit:
        url_path += "?limit=" + str(limit)
    result = base_request(url_path)
    return result


def get_sent_messages(id_customer, id=None):
    url_path = 'message_to_client/' + str(id_customer)
    if id:
        url_path += '/' + id
    result = base_request(url_path)
    return result


def send_message(id_customer, id_client, content):
    url_path = 'message_to_client/' + str(id_customer)
    info = {'sender': id_customer, 'receiver': id_client, 'content': content}
    result = base_post(url_path, info)
    return result.status_code == 201


def promotion_email_client(id_customer, id_client, id_promotion, id_location):
    url_path = 'promotion_email_client/' + str(id_customer) + '/' + str(id_client) + '/' + str(id_promotion) + '/' + str(id_location)
    info = {}
    result = base_post(url_path, info)
    return result.status_code == 201


def get_workplace_info(id_location, id_customer, username=None):
    if username:
        url_path = 'employee_workplace_info/' + str(id_customer) + '/' + str(id_location) + '/' + str(username)
    else:
        url_path = 'employee_workplace_info/' + str(id_customer) + '/' + str(id_location)

    result = base_request(url_path)
    return result


def save_workplace_info(info):
    url_path = 'employee_workplace_info/'
    result = base_post(url_path, info)
    return result.status_code == 204


def set_promotion_active_rest(id_promotion, active):
    url_path = 'set_promotion_active/' + str(id_promotion) + '/' + str(active)
    result = base_post(url_path, {})
    return result


def get_promotions(id_customer, id_promotion=None):
    url_path = 'promotions/' + str(id_customer)
    if id_promotion:
        url_path += '/' + str(id_promotion)
    result = base_request(url_path)
    return result


def get_ext_promotions(id_customer, id_promotion=None):
    url_path = 'external_promotions/' + str(id_customer)
    if id_promotion:
        url_path += '/' + str(id_promotion)
    result = base_request(url_path)
    return result


def get_promotion_preview(id_customer, id_promotion):
    url_path = 'promotion_preview/' + str(id_customer) + '/' + str(id_promotion)
    result = base_request_no_json(url_path)
    return result


def get_sp_promotion_preview(id_customer, id_promotion):
    url_path = 'sp_promotion_preview/' + str(id_customer) + '/' + str(id_promotion)
    result = base_request_no_json(url_path)
    return result


# External promotion test code
def get_ext_promotion_preview(id_customer, id_promotion):
    url_path = 'ext_promotion_preview/' + str(id_customer) + '/' + str(id_promotion)
    result = base_request_no_json(url_path)
    return result


def get_promotion_details(id_customer, id_promotion):
    url_path = 'promotion_details/' + str(id_customer) + '/' + str(id_promotion)
    result = base_request(url_path)
    return result


def get_sp_promotion_details(id_customer, id_promotion):
    url_path = 'sp_promotion_details/' + str(id_customer) + '/' + str(id_promotion)
    result = base_request(url_path)
    return result


def save_promotion(id_customer, info, id_promotion=None):
    url_path = 'promotions/' + str(id_customer)
    if id_promotion:
        url_path += '/' + str(id_promotion)
    result = base_post(url_path, info)
    return result.status_code == 200


def save_ext_promotion(id_customer, info, id_promotion=None):
    url_path = 'external_promotions/' + str(id_customer)
    if id_promotion:
        url_path += '/' + str(id_promotion)
    result = base_post(url_path, info)
    return result.status_code == 200


def save_promotion_location(id_customer, info, id_promotion=None):
    url_path = 'promotion_requests/' + str(id_customer)
    if id_promotion:
        url_path += '/' + str(id_promotion)
    result = base_post(url_path, info)
    return result.status_code == 200


def save_sp_promotion(id_customer, info, id_promotion=None):
    url_path = 'special_promotions/' + str(id_customer)
    if id_promotion:
        url_path += '/' + str(id_promotion)
    result = base_post(url_path, info)
    return result.status_code == 200


def get_locations(id_customer, external=None):
    url_path = 'locations/' + str(id_customer)
    if external:
        url_path += '/' + str(external)
    result = base_request(url_path)
    return result


# Find all categories
def get_all_categories():
    url_path = 'categories/'
    result = base_request(url_path)
    return result


# Find all categories
def get_all_countries():
    url_path = 'countries/'
    result = base_request(url_path)
    return result







def get_special_promotions(id_customer, id_sp_promotion=None):
    url_path = 'special_promotions/' + str(id_customer)
    if id_sp_promotion:
        url_path += '/' + str(id_sp_promotion)
    result = base_request(url_path)
    return result


def validate_promotion(validationstring):
    url_path = 'validate_promotion/' + str(validationstring)
    result = base_request(url_path)

    return result



def confirm_customer_admin(info):
    url_path = 'verify_customer_admin/'
    result = base_post(url_path, info)
    return result.status_code == 200


def create_customer(info):
    url_path = 'create_customer/'
    result = base_post(url_path, info)
    return result.status_code == 201


def update_sensor_location(info):
    url_path = 'update_sensor/'
    result = base_post(url_path, info)
    return result.status_code == 200


def get_stores(client_id, id_local=None):  # same as get_locations but with more attributes
    url_path = 'stores_list/' + str(client_id)
    if id_local:
        url_path += '/' + str(id_local)
    result = base_request(url_path)
    return result


def get_stores_by_client(client_id, id_local=None):  # same as get_locations but with more attributes
    url_path = 'stores_list/' + str(client_id)
    if id_local:
        url_path += '/' + str(id_local)
    result = base_request(url_path)
    return result



def save_store(client_id, local_info, id_local=None):
    url_path = 'stores/' + str(client_id)
    if id_local:
        url_path += '/' + str(id_local)
    result = base_post(url_path, local_info)
    return result.status_code == 200


def get_employees(id_customer, id_employee=None):
    url_path = 'employee_admin/' + str(id_customer)
    if id_employee:
        url_path += '/' + str(id_employee)
    result = base_request(url_path)
    return result


def get_employees_client(client_id, id_employee=None):
    url_path = 'employees_list/' + str(client_id)
    if id_employee:
        url_path += '/' + str(id_employee)
    result = base_request(url_path)
    return result


def save_employee(id_customer, employee_info, id_employee=None):
    url_path = 'employee_admin/' + str(id_customer)
    if id_employee:
        url_path += '/' + str(id_employee)
    result = base_post(url_path, employee_info)
    return result.status_code == 200

