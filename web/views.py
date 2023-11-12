from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import HttpResponse

from web.models import TimeSlot, TimeSlotTag, Holiday
from web.forms import RegistrationForm, AuthForm, TimeSlotForm, TimeSlotTagForm, HolidayForm

User = get_user_model()


def main_view(request):
    timeslots = TimeSlot.objects.all()
    return render(request, "web/main.html", {
        'timeslots': timeslots
    })


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


def auth_view(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Введены неверные данные")
            else:
                login(request, user)
                return redirect("main")
    return render(request, "web/auth.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("main")


def time_slot_edit_view(request, id=None):
    timeslot = TimeSlot.objects.get(id=id) if id is not None else None
    form = TimeSlotForm(instance=timeslot)
    if request.method == 'POST':
        form = TimeSlotForm(data=request.POST, files=request.FILES, instance=timeslot, initial={"user": request.user})
        if form.is_valid():
            form.save()
            return redirect("main")
    return render(request, "web/time_slot_form.html", {"form": form})


def _list_editor_view(request, model_cls, form_cls, template_name, url_name):
    items = model_cls.objects.all()
    form = form_cls()
    if request.method == 'POST':
        form = form_cls(data=request.POST, initial={"user": request.user})
        if form.is_valid():
            form.save()
            return redirect(url_name)
    return render(request, f"web/{template_name}.html", {"items": items, "form": form})


def tags_view(request):
    return _list_editor_view(request, TimeSlotTag, TimeSlotTagForm, "tags", 'tags')


def tags_delete_view(request, id):
    tag = TimeSlotTag.objects.get(id=id)
    tag.delete()
    return redirect('tags')


def holidays_view(request):
    return _list_editor_view(request, Holiday, HolidayForm, "holidays", 'holidays')


def holidays_delete_view(request, id):
    holiday = Holiday.objects.get(id=id)
    holiday.delete()
    return redirect('holiday')
