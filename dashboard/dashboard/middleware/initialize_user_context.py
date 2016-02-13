from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http.response import Http404
from django.utils.translation import LANGUAGE_SESSION_KEY
from dashboard.rest_gateway import get_context
from Bizwi_dashboard.settings import DATE_FORMATS


class Initialize(object):
    def process_request(self, request):
        """
        log in user and initialize session variables
        """

        try:
            session = request.session
            if request.user.is_authenticated():
                if not (session.get("name") and session.get("username") and session.get("id_location") and
                            session.get("id_customer") and session.get("time_zone")):
                    #session initialization
                    user = request.user
                    request.session["username"] = user.username

                    context = get_context(user.id)

                    is_customer_admin = context['is_customer_admin']
                    name = context['full_name']
                    id_location = context['id_location']
                    id_customer = context['id_customer']
                    customer_name = context['customer_name']
                    time_zone = context['timezone']
                    language = context['language']
                    date_format = DATE_FORMATS[language]

                    request.session["is_customer_admin"] = is_customer_admin
                    request.session["name"] = name
                    request.session["id_location"] = id_location
                    request.session["id_customer"] = id_customer
                    request.session["customer_name"] = customer_name

                    request.session["time_zone"] = time_zone
                    request.session[LANGUAGE_SESSION_KEY] = language  # Sets the language for the session
                    request.session["lang"] = language
                    request.session["date_format"] = date_format

        except Exception as e:
            request.session.flush()
            print e
            raise Http404