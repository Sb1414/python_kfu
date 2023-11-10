from django.urls import path

from web.views import main_view, registration_view

urlpatterns = [
    path("", main_view),
    path("registration/", registration_view),
]
