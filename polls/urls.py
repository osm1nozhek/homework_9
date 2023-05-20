from django.urls import path

from . import views

urlpatterns = [
    path("", views.add_number, name="add_number"),
    path("sms/", views.sms, name="sms"),
]
