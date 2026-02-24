from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from .models import Household, Person
from .forms import HouseholdForm, PersonForm


def list_households(request):
    households = Household.objects.all()
    return render(request, "Fortuneriseapp/household_list.html", {"households": households})

def edit_household(request, pk):
    household = get_object_or_404(Household, pk=pk)
    PersonFormSet = inlineformset_factory(Household, Person, form=PersonForm, extra=1, can_delete=True)
    if request.method == "POST":
        hform = HouseholdForm(request.POST, instance=household)
        formset = PersonFormSet(request.POST, instance=household)
        if hform.is_valid() and formset.is_valid():
            household = hform.save()
            people = formset.save(commit=False)
            for p in people:
                p.household = household
                p.save()
            for deleted in formset.deleted_objects:
                deleted.delete()
            return redirect("household_list")
    else:
        hform = HouseholdForm(instance=household)
        formset = PersonFormSet(instance=household)
    return render(request, "Fortuneriseapp/household_form.html", {"hform": hform, "formset": formset})

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
            return redirect("household_list")
    else:
        hform = HouseholdForm()
        formset = PersonFormSet()
    return render(request, "Fortuneriseapp/household_form.html", {"hform": hform, "formset": formset})


def household_success(request):
    return render(request, "Fortuneriseapp/household_success.html")