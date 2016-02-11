from django.shortcuts import render
from core_wrapper import *


def employees_list(request):
    client = request.session.get("client")
    employees = {'data': get_employees(client),
                      'customer_name': request.session.get("client_name")}
    if type(employees['data']) is not list:
        employees['data'] = []
    return render(request, 'employees.html', employees)
