from django.db import models

# Create your models here.

from django.db import models
class Household(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Person(models.Model):
    ROLE_CHOICES = [
        ("HUSBAND", "Husband"),
        ("WIFE", "Wife"),
        ("CHILD", "Child"),
        ("OTHER", "Other"),
    ]

    household = models.ForeignKey(
        Household,
        on_delete=models.CASCADE,
        related_name="members"
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.DateField(null=True, blank=True)

    job_type = models.CharField(max_length=100, blank=True)
    phone_no = models.CharField(max_length=15, blank=True)

    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"

class Income(models.Model):
    INCOME_TYPE = [
        ("SALARY", "Salary"),
        ("BUSINESS", "Business"),
        ("RENTAL", "Rental"),
        ("OTHER", "Other"),
    ]

    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    income_type = models.CharField(max_length=20, choices=INCOME_TYPE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    frequency = models.CharField(max_length=20)  # Monthly, Annual

class Debt(models.Model):
    DEBT_TYPE = [
        ("AUTO", "Auto Loan"),
        ("BOAT", "Boat Loan"),
        ("CREDIT_CARD", "Credit Card"),
        ("MEDICAL", "Medical"),
        ("PERSONAL", "Personal Loan"),
        ("STUDENT", "Student Loan"),
        ("OTHER", "Other"),
    ]

    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    owner = models.ManyToManyField(Person)  # husband, wife, or both
    debt_type = models.CharField(max_length=20, choices=DEBT_TYPE)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.FloatField()
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2)

class Mortgage(models.Model):
    PROPERTY_TYPE = [
        ("PRIMARY", "Primary Residence"),
        ("SECOND", "Second Home"),
        ("RENTAL", "Rental Property"),
        ("TIMESHARE", "Time Share"),
        ("HELOC", "HELOC"),
    ]

    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.FloatField()
    
    
class ChildExpense(models.Model):
    EXPENSE_TYPE = [
        ("EDUCATION", "Education"),
        ("CHILDCARE", "Child Care"),
    ]

    child = models.ForeignKey(Person, on_delete=models.CASCADE)
    expense_type = models.CharField(max_length=20, choices=EXPENSE_TYPE)
    annual_cost = models.DecimalField(max_digits=10, decimal_places=2)


class Asset(models.Model):
    ASSET_CATEGORY = [
        ("FIXED", "Fixed Asset"),
        ("VARIABLE", "Variable Asset"),
        ("INDEXED", "Indexed Asset"),
    ]

    ASSET_TYPE = [
        # Fixed
        ("BOND", "Bond"),
        ("CD", "CD"),
        ("CHECKING", "Checking"),
        ("SAVINGS", "Savings"),
        ("MONEY_MARKET", "Money Market"),

        # Variable
        ("BITCOIN", "Bitcoin"),
        ("MUTUAL_FUND", "Mutual Fund"),
        ("STOCK", "Stock"),
        ("OPTION", "Option"),
        ("HSA", "HSA"),
        ("ANNUITY", "Annuity"),
        ("IRA", "IRA"),
        ("401K", "401K"),
        ("403B", "403B"),
        ("PENSION", "Pension"),
        ("SOLO_401K", "Solo 401K"),
        ("SEP_IRA", "SEP IRA"),
        ("SIMPLE_IRA", "SIMPLE IRA"),
        ("ROTH_IRA", "ROTH IRA"),
        ("PLAN_529", "529"),

        # Indexed
        ("IUL", "IUL CV"),
        ("FIA", "FIA"),
    ]

    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    owner = models.ManyToManyField(Person)
    category = models.CharField(max_length=10, choices=ASSET_CATEGORY)
    asset_type = models.CharField(max_length=20, choices=ASSET_TYPE)
    value = models.DecimalField(max_digits=12, decimal_places=2)


class LifeInsurance(models.Model):
    POLICY_TYPE = [
        ("TERM", "Term"),
        ("PERM", "Permanent"),
        ("WL", "Whole Life"),
    ]

    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    insured = models.ForeignKey(Person, on_delete=models.CASCADE)
    policy_type = models.CharField(max_length=10, choices=POLICY_TYPE)
    cash_value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    coverage_amount = models.DecimalField(max_digits=12, decimal_places=2)

