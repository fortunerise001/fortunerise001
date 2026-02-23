from django.urls import path
from django.shortcuts import redirect
from . import household_views

urlpatterns = [
    # root displays household list
    path("", household_views.list_households, name="household_list"),
    path("household/new/", household_views.create_household, name="create_household"),
    path("household/<int:pk>/edit/", household_views.edit_household, name="edit_household"),
    path("household/success/", household_views.household_success, name="household_success"),
]