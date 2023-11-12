from django import forms
from django.contrib.auth import get_user_model

from web.models import TimeSlot, TimeSlotTag, Holiday

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            self.add_error("password", "Пароли не совпадают")
        return cleaned_data

    class Meta:
        model = User
        fields = ("email", "username", "password", "password2")


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class TimeSlotForm(forms.ModelForm):
    def save(self, commit=True):
        if not self.cleaned_data['end_date']:
            self.instance.is_realtime = True
        self.instance.user = self.initial['user']
        return super().save(commit)

    class Meta:
        model = TimeSlot
        fields = ('title', 'start_date', 'end_date', 'image', 'tags')
        widgets = {
            "start_date": forms.DateTimeInput(
                attrs={"type": "datetime-local"}, format='%Y-%m-%dT%H:%M'
            ),
            "end_date": forms.DateTimeInput(
                attrs={"type": "datetime-local"}, format='%Y-%m-%dT%H:%M'
            )
        }


class TimeSlotTagForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit)

    class Meta:
        model = TimeSlotTag
        fields = ('title', )


class HolidayForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit)

    class Meta:
        model = Holiday
        fields = ('date', )
        widgets = {
            "date": forms.DateTimeInput(attrs={"type": "date"}, format='%Y-%m-%d')
        }
