from django.urls import path
from .views import getBills, deleteBill, createBill, updateBillStatus

urlpatterns = [
    path('', getBills.as_view(), name='expense-list'),
    path('create', createBill.as_view(), name='expense-create'),
    path('delete/<int:pk>', deleteBill.as_view(), name='expense-delete'),
    path('updatestatus', updateBillStatus.as_view(), name='income-total'),
]
