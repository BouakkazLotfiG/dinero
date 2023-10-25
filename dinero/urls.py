
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expense/', include('expenses.urls')),
    path('income/', include('income.urls')),
    path('bills/', include('bills.urls')),
]
