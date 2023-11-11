from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse

User = get_user_model()

from web.forms import RegistrationForm


def main_view(request):
    return render(request, "web/main.html")


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
            )
            # чтобы записать хэш пароля в бд
            user.set_password(form.cleaned_data['password'])
            user.save()
            is_success = True
            print(form.cleaned_data)
    return render(request, "web/registration.html", {
        "form": form, "is_success": is_success}
    )