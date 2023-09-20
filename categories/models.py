from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    ignore = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    
    
class BudgetByCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    spend_budget = models.DecimalField(max_digits=10, decimal_places=2)
    total_budget = models.DecimalField(max_digits=10, decimal_places=2)
    avaible = models.BooleanField(default=True)
    name_category = models.CharField(max_length=100)

    def __str__(self):
        return self.name_category
    