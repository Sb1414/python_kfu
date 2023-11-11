from django.urls import path

from web.views import main_view, registration_view, auth_view

urlpatterns = [
    path("", main_view, name="main"),
    path("registration/", registration_view, name="registration"),
    path("auth/", auth_view, name="auth"),
]
