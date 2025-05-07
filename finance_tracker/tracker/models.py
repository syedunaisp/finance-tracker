from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    TRANSACTION_TYPE = [('income', 'Income'), ('expense', 'Expense')]
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPE)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)