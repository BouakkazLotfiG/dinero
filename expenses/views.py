from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Expense
from .serializers import ExpenseSerializer
from django.http import Http404
from django.db.models import Sum

class getExpenses(APIView):
    """
    List all expenses.
    """

    def get(self, request, format=None):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

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
    """
    Retrieve the total expenses.
    """

    def get(self, request, format=None):
        total_expenses = Expense.objects.aggregate(total=Sum('amount'))['total']
        if total_expenses is None:
            total_expenses = 0  # Set the total expenses to 0 if there are no expense entries.
        return Response({'total_expenses': total_expenses})
