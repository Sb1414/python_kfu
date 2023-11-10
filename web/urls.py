from django.urls import path

from web.views import main_view

urlpatterns = [
    path("", main_view),
]
