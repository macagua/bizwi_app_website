# coding=utf-8
from django.http import JsonResponse, HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from core_wrapper import *
from .settings import APP_OWNER, APP_NAME, LANGUAGE_LIST, DATE_FORMATS, LOGIN_URL
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .settings import APP_OWNER, APP_NAME
from .forms import AdminForm, ClientForm, StoreForm, BrandForm, EmployeeForm, SettingsEmployeeForm
import pytz
import json
import sys

# Parameter basics
DEFAULT_APP_CONTEXT = {'title': APP_OWNER, 'name': APP_NAME, }


def index(request):
    if request.user.is_authenticated():
        return redirect('done')
        # context = RequestContext(request, {'request': request, 'user': request.user})
    context = RequestContext(request, DEFAULT_APP_CONTEXT)
    return render_to_response('home.html', context_instance=context)


def only_employee(login_url):
    def decorator(a_view):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated() and not request.session.get("is_customer_admin"):
                return a_view(request, *args, **kwargs)
            if len(request.GET) > 0:
                params = '?'
                for k, v in request.GET.items():
                    params = params + k + '=' + v + '&'
                params = params[:-1]
                return HttpResponseRedirect(LOGIN_URL + '?next=' + request.path + params)
            else:
                return HttpResponseRedirect(LOGIN_URL + '?next=' + request.path)
        return _wrapped_view
    return decorator


def extra_info(the_func):
    def _decorated(request, *args, **kwargs):
        id_customer = request.session.get("id_customer")
        id_location = request.session.get("id_location")
        customer_name = request.session.get("customer_name")
        messages = get_messages(id_customer, limit=3)
        birthdays = get_today_birthdays(id_location)
        next_birthdays_count = birthdays[0]
        promotion_location = get_promotion_requests(id_customer)
        del birthdays[0]
        extrainfo = {'messages_count': messages[0],
                     'customer_name': customer_name,
                     'preview_messages': messages[1:],
                     'birthdays': birthdays,
                     'next_birthdays_count': next_birthdays_count,
                     'promotion_requests': promotion_location,
                     }
        kwargs['extra_info'] = extrainfo
        return the_func(request, *args, **kwargs)
    return _decorated


@login_required
def done(request):
    is_client_admin = request.session.get("is_client_admin")

    if is_client_admin:
        customer = request.session.get("id_customer")
        if customer:
            # go to admin dashboard
            return redirect("locals_admin")
        else:
            # go to customer creation
            return redirect("new_customer")
    else:
        # go to dashboard
        return redirect("home")


def logout(request):
    """Logs out user"""
    auth_logout(request)
    request.session.flush()
    return redirect('index')


@only_employee(LOGIN_URL)
#@extra_info
#def dashboard(request, extra_info):
def dashboard(request):
#    id_location = request.session.get("id_location")
#    stats = get_stats(id_location)
#
#    # create context
#    info = {
#        'unique_users': stats["unique_users"],
#        'recurring': stats["recurring"],
#        'pedestrians': stats["pedestrians"],
#        'visitors': stats["visitors"],
#        'impacts': stats["impacts"],
#        'check_ins': stats["check_ins"],
#    }
#
#    info.update(extra_info)
#    return render(request, 'dashboard.html', info)
    return render(request, 'dashboard.html')


# Registration new clients

def new_client_admin(request):
    form = AdminForm()
    info = {}

    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            client_name = form.cleaned_data['client_name']
            telephone = form.cleaned_data['telephone']

            info = {
                'name': name,
                'lastname': lastname,
                'username': username,
                'email': email,
                'password': password,
                'client_name': client_name,
                'telephone': telephone,
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


def stores(request):
    client = request.user.id
    stores_list = {'data': get_stores(client)}
    if type(stores_list['data']) is not list:
        stores_list['data'] = []

    print stores_list

    return render(request, 'stores.html', stores_list)


# Select store o push post
def store(request, id_local=None):
    form = StoreForm()
    client_id = request.user.id
    info = {'client_id': request.user.id}
    if request.method == 'POST':
        form = StoreForm(request.POST)

        if form.is_valid():
            local_info = {
                'name': form.cleaned_data['name'],
                'telephone': form.cleaned_data['telephone'],
                'web_site': form.cleaned_data['web_site'],
                'description': form.cleaned_data['description'],
                'country': form.cleaned_data['country'],
                'city': form.cleaned_data['city'],
                'region': form.cleaned_data['region'],
                'address': form.cleaned_data['address'],
                'logo_url': form.cleaned_data['logo_url'],
                'background_color': form.cleaned_data['background_color'],
                'foreground_color': form.cleaned_data['foreground_color'],
                'background_img': form.cleaned_data['background_img'],
                'ttf_font': form.cleaned_data['ttf_font'],
            }
            if id_local:
                result = save_store(client_id, local_info, id_local)
                info['page'] = "update"
                info['local'] = local_info
            else:
                result = save_store(client_id, local_info)
                info['page'] = "add"

            if result:
                info['success'] = True
            else:
                info['error'] = True
                info['local'] = local_info
        else:
            info['error'] = True
            info['form'] = form
            info['local'] = form.data
            if id_local:
                info['page'] = "update"
            else:
                info['page'] = "add"

    if request.method == 'GET':
        if id_local:
            info['page'] = "update"
            local = get_stores(client_id, id_local)
            if local:
                info['local'] = local
            else:
                raise Http404
        else:
            info['page'] = "add"

    return render(request, 'store_basic.html', info)


def employees_list(request):
    client = request.session.get("client")
    employees = {'data': get_employees(client),
                 'customer_name': request.session.get("client_name")}
    if type(employees['data']) is not list:
        employees['data'] = []
    return render(request, 'employees_admin.html', employees)




def employee(request, id_employee=None):
    id_customer = request.session.get("id_customer")
    locations_list = get_stores(id_customer)
    info = {'customer_name': request.session.get("customer_name"),
            'languages': LANGUAGE_LIST,
            'stores': stores}

    if request.method == 'POST':

        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee_info = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'phone': form.cleaned_data['phone'],
                'language': form.cleaned_data['language'],
                'stores': str(form.cleaned_data['stores']),
                'checkpass': str(form.cleaned_data['checkpass']),
                'password': str(form.cleaned_data['password']),
            }
            if id_employee:
                result = save_employee(id_customer, employee_info, id_employee)
                info['page'] = "update"
                info['employee'] = employee_info
            else:
                result = save_employee(id_customer, employee_info)
                info['page'] = "add"

            if result:
                info['success'] = True
            else:
                info['error'] = True
                info['employee'] = employee_info
        else:
            info['error'] = True
            info['form'] = form
            info['employee'] = form.data
            if id_employee:
                info['page'] = "update"
            else:
                info['page'] = "add"

    if request.method == 'GET':
        if id_employee:
            info['page'] = "update"
            employee = get_employees(id_customer, id_employee)
            if employee:
                info['employee'] = employee
            else:
                raise Http404
        else:
            info['page'] = "add"

    return render(request, 'employee_admin.html', info)


def settings_employee(request):
    id_location = '0'
    id_customer = request.session.get("id_customer")
    customer_name = request.session.get("customer_name")

    form = SettingsEmployeeForm()
    info = {}
    user = request.session["username"]

    if request.method == 'POST':
        form = SettingsEmployeeForm(request.POST)
        lang_ok = False
        for l in LANGUAGE_LIST:
            if l == form.data['language']:
                lang_ok = True
        if form.is_valid() and lang_ok:
            url = form.cleaned_data['url']
            description = form.cleaned_data['description']
            time_zone = form.cleaned_data['time_zone']
            language = form.cleaned_data['language']
            img_url = form.cleaned_data['image']
            cover_img_url = form.cleaned_data['cover_image']
            uppercolor = form.cleaned_data['uppercolor']
            lowercolor = form.cleaned_data['lowercolor']
            info = {'id_customer': id_customer,
                    'id_location': id_location,
                    'url': url,
                    'img_url': img_url,
                    'cover_img_url': cover_img_url,
                    'description': description,
                    'time_zone': time_zone,
                    'language': language,
                    'username': user,
                    'uppercolor': uppercolor,
                    'lowercolor': lowercolor,
            }

            result = save_workplace_info(info)

            if result:
                info['success'] = True
                request.session["time_zone"] = time_zone
                request.session[LANGUAGE_SESSION_KEY] = language
                request.session["lang"] = language
                request.session["date_format"] = DATE_FORMATS[language]
            else:
                info['error'] = True
                info['url'] = url
                info['description'] = description
                info['time_zone'] = time_zone
                info['language'] = language
                info['img_url'] = img_url
                info['cover_img_url'] = cover_img_url
                info['uppercolor'] = uppercolor
                info['lowercolor'] = lowercolor
        else:
            info = form.cleaned_data
            info['img_url'] = form.cleaned_data['image']
            info['error'] = True

    elif request.method == 'GET':
        info = get_workplace_info(id_location, id_customer, user)

    info['form'] = form
    info['timezones'] = pytz.common_timezones
    info['time_zone'] = request.session.get("time_zone")
    info['customer_name'] = customer_name
    info['languages'] = LANGUAGE_LIST

    return render(request, 'settings_employee.html', info)

@only_employee(LOGIN_URL)
#@extra_info
#def profile_edit(request, extra_info):
def profile_edit(request):
    employee_id = request.user.id
    employee_info = get_info(employee_id)
    email = employee_info['email']

    info = {}

    if request.method == 'POST':
        if "profileForm" in request.POST:
            form = ProfileForm(request.POST)

            if form.is_valid():
                try:
                    email = form.cleaned_data['email']
                    employee_info['email'] = email
                    result = save_info(employee_id, employee_info)
                    if result:
                        info['save_success'] = True
                    else:
                        info['save_error'] = True
                        info['form'] = form

                except Exception as e:
                    print e
                    info['save_error'] = True
                    info['form'] = form
            else:
                info['save_error'] = True
                info['form'] = form

        elif "changePasswordForm" in request.POST:
            form = SetPasswordForm(request.user, request.POST)
            if form.is_valid():
                try:
                    new_password = form.cleaned_data['new_password1']
                    result = change_password(employee_id, new_password)
                    if result:
                        info['change_success'] = True
                except Exception as e:
                    print e
                    info['change_error'] = True
                    info['form'] = form
            else:
                info['change_error'] = True
                info['form'] = form

    info['email'] = email
    #info.update(extra_info)
    return render(request, 'profile_form.html', info)


