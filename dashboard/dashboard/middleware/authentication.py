from django.contrib.auth.models import User
from dashboard.rest_gateway import auth, get_info


class CoreBackend(object):
    """
    Authenticates against Core
    """

    def authenticate(self, username=None, password=None):
        response = auth(username, password)

        if response.status_code == 200:
            result = response.json()
            if not result['error']:
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    user_json = result['user']
                    user = User(id=user_json['id'], username=user_json['username'])
                    user.save()
                return user
        return None

    def get_user(self, user_id):
        try:
            user_json = get_info(user_id)
            return User.objects.get(id=user_id)
            #return User(id=user_json['id'], username=user_json['username'])
        except User.DoesNotExist as e:
            print e
            return None