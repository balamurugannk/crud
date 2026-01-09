from django.db import models

class Expense(models.Model):

    expense_id = models.CharField(max_length=100)
    date = models.DateField()
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    payment_mode = models.CharField(max_length=100)
    merchant_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    notes = models.TextField()
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.category