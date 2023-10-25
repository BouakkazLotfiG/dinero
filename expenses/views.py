from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Expense
from .serializers import ExpenseSerializer
from django.http import Http404
from django.db.models import Sum
from rest_framework.pagination import PageNumberPagination

class getExpenses(APIView):
    """
    List all expenses.
    """

    def get(self, request, format=None):
        paginator = PageNumberPagination()
        expenses = Expense.objects.all()
        result_page = paginator.paginate_queryset(expenses, request)
        serializer = ExpenseSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class createExpense(APIView):
    """
    Create a new expense.
    """

    def post(self, request, format=None):
        serializer = ExpenseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class deleteExpense(APIView):
 

    def delete(self, request, pk, format=None):
        expense = self.get_object(pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Include the get_object method to retrieve the expense
    def get_object(self, pk):
        try:
            return Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            raise Http404

class TotalExpense(APIView):
    def get(self, request, format=None):
        total_expense = Expense.objects.aggregate(total=Sum('amount'))
        return Response({'total_expense': total_expense['total']})
