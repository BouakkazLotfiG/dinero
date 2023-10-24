from django.urls import path
from .views import getExpenses, createExpense, deleteExpense

urlpatterns = [
    path('', getExpenses.as_view(), name='expense-list'),
    path('create', createExpense.as_view(), name='expense-create'),
    path('delete/<int:pk>', deleteExpense.as_view(), name='expense-delete'),
]
