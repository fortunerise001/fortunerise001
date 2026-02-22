from django.urls import path
from django.shortcuts import redirect
from . import household_views

urlpatterns = [
    # redirect base URL to the form
    path("", lambda request: redirect("create_household")),
    path("household/new/", household_views.create_household, name="create_household"),
    path("household/success/", household_views.household_success, name="household_success"),
]