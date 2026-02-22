from django import forms
from django.forms import ModelForm
from .models import Household, Person


class HouseholdForm(ModelForm):
    class Meta:
        model = Household
        fields = ["name"]


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = [
            "role",
            "first_name",
            "last_name",
            "gender",
            "dob",
            "job_type",
            "phone_no",
            "address",
            "city",
            "state",
            "country",
        ]
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date"}),
        }
from django import forms
from django.forms import ModelForm
from .models import Household, Person


class HouseholdForm(ModelForm):
    class Meta:
        model = Household
        fields = ["name"]


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = [
            "role",
            "first_name",
            "last_name",
            "gender",
            "dob",
            "job_type",
            "phone_no",
            "address",
            "city",
            "state",
            "country",
        ]
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date"}),
        }
