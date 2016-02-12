from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from core_wrapper import *
from .settings import APP_OWNER, APP_NAME
from .forms import AdminForm

# Parameter basics
DEFAULT_APP_CONTEXT = {'title': APP_OWNER, 'name': APP_NAME, }


def index(request):
    if request.user.is_authenticated():
        return redirect('done')
        # context = RequestContext(request, {'request': request, 'user': request.user})
    context = RequestContext(request, DEFAULT_APP_CONTEXT)
    return render_to_response('home.html', context_instance=context)


# Registration new clients
def new_client_admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            info = {
                'name': name,
                'lastname': lastname,
                'username': username,
                'email': email,
                'password': password,
                'is_active': True,
            }

            # Call to wrapper
            result = create_client_admin(info)

            if result['success']:
                info['success'] = True
                return render(request, 'successful_admin_creation.html')
            else:
                if result['error'] == 'duplicate_email':
                    info['error_string'] = _("Failed to save your data. The email is already in use.")
                if result['error'] == 'duplicate_username':
                    info['error_string'] = _("Failed to save your data. The username is already in use.")
                info['error'] = True
                info['form'] = form
        else:
            info['error'] = True
            info['form'] = form

    return render(request, 'new_admin.html', info)


def employees_list(request):
    client = request.session.get("client")
    employees = {'data': get_employees(client),
                 'customer_name': request.session.get("client_name")}
    if type(employees['data']) is not list:
        employees['data'] = []
    return render(request, 'employees.html', employees)
