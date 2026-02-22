from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Household,
    Person,
    Income,
    Debt,
    Mortgage,
    ChildExpense,
    Asset,
    LifeInsurance,
)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "role",
        "household",
        "phone_no",
    )
    list_filter = ("role", "household")
    search_fields = ("first_name", "last_name", "phone_no")

@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = (
        "household",
        "owner",
        "income_type",
        "amount",
        "frequency",
    )
    list_filter = ("income_type", "frequency")
    search_fields = ("owner__first_name", "owner__last_name")


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = (
        "debt_type",
        "household",
        "balance",
        "interest_rate",
        "monthly_payment",
    )
    list_filter = ("debt_type",)
    filter_horizontal = ("owner",)
@admin.register(Mortgage)
class MortgageAdmin(admin.ModelAdmin):
    list_display = (
        "property_type",
        "household",
        "balance",
        "interest_rate",
    )
    list_filter = ("property_type",)

@admin.register(ChildExpense)
class ChildExpenseAdmin(admin.ModelAdmin):
    list_display = (
        "child",
        "expense_type",
        "annual_cost",
    )
    list_filter = ("expense_type",)
    search_fields = ("child__first_name", "child__last_name")

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = (
        "asset_type",
        "category",
        "household",
        "value",
    )
    list_filter = ("category", "asset_type")
    filter_horizontal = ("owner",)
@admin.register(LifeInsurance)
class LifeInsuranceAdmin(admin.ModelAdmin):
    list_display = (
        "policy_type",
        "insured",
        "household",
        "coverage_amount",
        "cash_value",
    )
    list_filter = ("policy_type",)
    search_fields = ("insured__first_name", "insured__last_name")
