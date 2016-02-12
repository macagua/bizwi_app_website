from django.http import JsonResponse, HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from core_wrapper import *
from .settings import APP_OWNER, APP_NAME
from .forms import AdminForm, ClientForm
import pytz

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
    info = {}

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

    return render(request, 'new_client_admin.html', info)


def confirm_client(request, username, code):
    try:
        # To Wrapper
        result = confirm_client_admin({'username': username, 'confirmation_code': code})

        if result:
            return redirect('login')
        else:
            raise Http404
    except Exception as e:
        print e
        raise Http404


def new_client(request):
    form = ClientForm()
    info = {}

    if request.method == 'POST':
        form = ClientForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            url = form.cleaned_data['url']
            time_zone = form.cleaned_data['time_zone']
            img_url = form.cleaned_data['image']

            info = {
                'id_admin': request.user.id,
                'name': name,
                'url': url,
                'description': description,
                'time_zone': time_zone,
                'img_url': img_url,
            }

            result = create_client(info)

            if result:
                info['success'] = True
                return redirect('dashboard_admin')
            else:
                info['error'] = True
        else:
            info['error'] = True
            info['form'] = form

    info['timezones'] = pytz.common_timezones
    info['form'] = form

    return render(request, 'new_client.html', info)


def employees_list(request):
    client = request.session.get("client")
    employees = {'data': get_employees(client),
                 'customer_name': request.session.get("client_name")}
    if type(employees['data']) is not list:
        employees['data'] = []
    return render(request, 'employees.html', employees)
