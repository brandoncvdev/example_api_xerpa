from rest_framework import generics
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import BudgetByCategory, Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer, BudgetByCategorySerializer
# from categories import models

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


@api_view(['GET'])
def budgets_by_category(request):
    if request.method == 'GET': 
        transactions = Transaction.objects.filter(ignore=False)
        categories = Category.objects.all()
        data = []
        for category_item in categories:
            for transaction in transactions:
                total_transaction = 0
                if not transaction.ignore:
                    total_transaction += transaction.amount
            budgetAvaible = category_item.limit >= total_transaction
            budget = BudgetByCategory(
                    category=category_item,
                    spend_budget=total_transaction,
                    total_budget=category_item.limit,
                    avaible=budgetAvaible,
                    name_category=category_item.name
            )
            budget.save()
            data.append({
                'category': budget.category,
                'spend_budget': budget.spend_budget, 
                'total_budget': budget.total_budget,
                'avaible': budget.avaible,
                'name_category': budget.name_category
            })
        serializer = BudgetByCategorySerializer(data, many=True)
        return Response(serializer.data)