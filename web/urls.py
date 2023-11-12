from django.urls import path

from web.views import main_view, registration_view, auth_view, logout_view, time_slot_edit_view, tags_view, \
    tags_delete_view, holidays_view, holidays_delete_view, time_slot_delete_view, time_slot_stop_view

urlpatterns = [
    path("", main_view, name="main"),
    path("registration/", registration_view, name="registration"),
    path("auth/", auth_view, name="auth"),
    path("logout/", logout_view, name="logout"),
    path("time_slots/add/", time_slot_edit_view, name="time_slot_add"),
    path("time_slots/<int:id>/", time_slot_edit_view, name="time_slot_edit"),
    path("time_slots/<int:id>/delete/", time_slot_delete_view, name="time_slot_delete"),
    path("time_slots/<int:id>/stop/", time_slot_stop_view, name="time_slot_stop"),
    path("tags/", tags_view, name="tags"),
    path("tags/<int:id>/delete/", tags_delete_view, name="tags_delete"),
    path("holidays/", holidays_view, name="holidays"),
    path("holidays/<int:id>/delete/", holidays_delete_view, name="holidays_delete"),
]
