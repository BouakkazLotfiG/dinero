from django.urls import path
from .views import getExpenses, createExpense, deleteExpense, TotalExpense

urlpatterns = [
    path('', getExpenses.as_view(), name='expense-list'),
    path('create', createExpense.as_view(), name='expense-create'),
    path('delete/<int:pk>/', deleteExpense.as_view(), name='expense-delete'),
    path('total', TotalExpense.as_view(), name='expense-total'),
]
