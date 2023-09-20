from django.urls import path, include

from categories.views import CategoryListCreateView, CategoryRetrieveUpdateDestroyView, TransactionListCreateView, TransactionRetrieveUpdateDestroyView, budgets_by_category  # noqa: E501

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-retrieve-update-destroy'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionRetrieveUpdateDestroyView.as_view(), name='transaction-retrieve-update-destroy'),
    path('budgets/', budgets_by_category, name='budget-list'),
]
