from django.urls import path
from .views import createIncome, deleteIncome, getIncome

urlpatterns = [
    path('', getIncome.as_view(), name='income-list'),
    path('create', createIncome.as_view(), name='income-create'),
    path('delete/<int:pk>', deleteIncome.as_view(), name='income-delete'),
]
