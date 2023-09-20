from rest_framework import serializers
from .models import Category, Transaction, BudgetByCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('__all__')

class BudgetByCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetByCategory
        fields = ('__all__')