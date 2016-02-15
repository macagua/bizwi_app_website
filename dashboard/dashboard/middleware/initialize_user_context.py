from django.http.response import Http404
from dashboard.core_wrapper import get_context


class Initialize(object):
    def process_request(self, request):
        """
        log in user and initialize session variables
        """

        try:
            session = request.session
            if request.user.is_authenticated():
                if not (session.get("name") and session.get("username") and session.get("time_zone")):
                    #session initialization
                    user = request.user
                    request.session["username"] = user.username

                    context = get_context(user.id)

                    is_client_admin = context['is_client_admin']
                    first_name = context['first_name']
                    last_name = context['last_name']

                    request.session["is_client_admin"] = is_client_admin
                    request.session["name"] = first_name+" "+last_name

                    """
                    request.session[LANGUAGE_SESSION_KEY] = language  # Sets the language for the session
                    request.session["lang"] = language
                    request.session["date_format"] = date_format
                    """

        except Exception as e:
            request.session.flush()
            print e
            raise Http404