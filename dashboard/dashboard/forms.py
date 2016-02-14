from django import forms


class AdminForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    lastname = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=255, required=True)
    client_name = forms.CharField(max_length=255, required=True)
    telephone = forms.CharField(max_length=255, required=True)
    password1 = forms.CharField()
    password2 = forms.CharField()

    def clean(self):
        cleaned_data = super(AdminForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2:
            # Only do something if both fields are valid so far.
            if password1 != password2:
                self.add_error('password2', "The two password fields didn't match.")

        return cleaned_data


class CustomUserForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    gender = forms.CharField(max_length=255)
    birthday = forms.CharField()
    lang = forms.CharField(max_length=2)


class EmployeeForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=200)
    language = forms.CharField(max_length=2)
    location = forms.DecimalField(min_value=0)
    password = forms.CharField(max_length=100)
    checkpass = forms.BooleanField(initial=False, required=False)



class ClientForm(forms.Form):
    client_name = forms.CharField(max_length=255, required=False)
    telephone = forms.CharField(max_length=255, required=False)
    web_site = forms.CharField(max_length=255, required=False)
    logo_url = forms.CharField(max_length=255, required=False)
    background_color = forms.CharField(max_length=255, required=False)
    foreground_color = forms.CharField(max_length=255, required=False)
    background_img = forms.CharField(max_length=255, required=False)
    ttf_font = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=255, required=False)
    country = forms.CharField(max_length=255, required=False)
    photo_url = forms.CharField(max_length=255, required=False)
    facebook_fan_page = forms.CharField(max_length=255, required=False)
    twitter_account = forms.CharField(max_length=255, required=False)
    language = forms.CharField(max_length=255, required=False)
    gplus_id = forms.CharField(max_length=255, required=False)
    timezone = forms.CharField(max_length=255, required=False)
    description = forms.CharField(max_length=255, required=False)
    url = forms.URLField(max_length=255, required=False)
    timezone = forms.CharField(max_length=255, required=False)


class BrandForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    description = forms.CharField()
    url = forms.URLField(max_length=255)
    time_zone = forms.CharField(max_length=255)


class StoreForm(forms.Form):
    name = forms.CharField(max_length=100)
    telephone = forms.CharField(max_length=100)
    web_site = forms.CharField(max_length=100)
    description = forms.CharField(max_length=250)
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    region = forms.CharField(max_length=100)
    address = forms.CharField(max_length=200)
    logo_url = forms.CharField(max_length=400)
    background_color = forms.CharField(max_length=10)
    foreground_color = forms.CharField(max_length=10)
    background_img = forms.CharField(max_length=10)
    ttf_font = forms.URLField()


class SettingsEmployeeForm(forms.Form):
    url = forms.URLField(max_length=255)
    description = forms.CharField()
    time_zone = forms.CharField(max_length=255)
    language = forms.CharField(max_length=2)
    #image = forms.URLField(widget=S3DirectWidget(dest='imgs_customer'), required=False)
    #cover_image = forms.URLField(widget=S3DirectWidget(dest='imgs_customer'), required=False)
    uppercolor = forms.CharField(max_length=7)
    lowercolor = forms.CharField(max_length=7)
