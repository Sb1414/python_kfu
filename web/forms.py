from django import forms

class RegistrationForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.EmailField(widget=forms.PasswordInput)
    password2 = forms.EmailField(widget=forms.PasswordInput)

    def clean(self):
        cleane_data = super().clean()
        if cleane_data['password'] != cleane_data['password2']:
            self.add_error("password", "Пароли не совпадают")
        return cleane_data