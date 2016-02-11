from django.shortcuts import render
from dashboard.dashboard.core_wrapper import *


def employees_list(request):
    client = request.session.get("client")
    employees = {'data': get_employees(client),
                      'customer_name': request.session.get("client_name")}
    if type(employees['data']) is not list:
        employees_list['data'] = []
    return render(request, 'employees_list.html', employees)





def all_employees(request):
    employees = {'data': get_employees(client),
                      'customer_name': request.session.get("customer_name")}
    if type(employees_list['data']) is not list:
        employees_list['data'] = []
    return render(request, 'employees_admin.html', employees_list)