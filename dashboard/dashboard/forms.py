from django import forms


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


class ClientForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    description = forms.CharField()
    url = forms.URLField(max_length=255)
    time_zone = forms.CharField(max_length=255)


