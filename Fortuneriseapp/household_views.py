from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import Household, Person
from .forms import HouseholdForm, PersonForm


def create_household(request):
    PersonFormSet = inlineformset_factory(Household, Person, form=PersonForm, extra=3, can_delete=True)
    if request.method == "POST":
        hform = HouseholdForm(request.POST)
        formset = PersonFormSet(request.POST)
        if hform.is_valid() and formset.is_valid():
            household = hform.save()
            people = formset.save(commit=False)
            for p in people:
                p.household = household
                p.save()
            # handle deleted forms
            for deleted in formset.deleted_objects:
                deleted.delete()
            return redirect("household_success")
    else:
        hform = HouseholdForm()
        formset = PersonFormSet()
    return render(request, "Fortuneriseapp/household_form.html", {"hform": hform, "formset": formset})


def household_success(request):
    return render(request, "Fortuneriseapp/household_success.html")