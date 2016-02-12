from django import forms


class AdminForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    lastname = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=255, required=True)
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
    name = forms.CharField(max_length=255, required=True)
    description = forms.CharField()
    url = forms.URLField(max_length=255)
    time_zone = forms.CharField(max_length=255)


class BrandForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    description = forms.CharField()
    url = forms.URLField(max_length=255)
    time_zone = forms.CharField(max_length=255)


class StoreForm(forms.Form):
    name = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    region = forms.CharField(max_length=100)
    address = forms.CharField(max_length=200)
    latitude = forms.DecimalField(decimal_places=5, max_digits=7)
    longitude = forms.DecimalField(decimal_places=5, max_digits=8)
    distance_threshold = forms.DecimalField(min_value=0)
    logo_url = forms.CharField(max_length=400)
    background_color = forms.CharField(max_length=10)
    foreground_color = forms.CharField(max_length=10)
    ttf_font = forms.CharField(max_length=400)


class SettingsEmployeeForm(forms.Form):
    url = forms.URLField(max_length=255)
    description = forms.CharField()
    time_zone = forms.CharField(max_length=255)
    language = forms.CharField(max_length=2)
    #image = forms.URLField(widget=S3DirectWidget(dest='imgs_customer'), required=False)
    #cover_image = forms.URLField(widget=S3DirectWidget(dest='imgs_customer'), required=False)
    uppercolor = forms.CharField(max_length=7)
    lowercolor = forms.CharField(max_length=7)
