import pytz

from django.utils import timezone


class TimezoneMiddleware(object):
    def process_request(self, request):
        time_zone = request.session.get("time_zone")
        if time_zone:
            timezone.activate(pytz.timezone(time_zone))
        else:
            timezone.deactivate()
