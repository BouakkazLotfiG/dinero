from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Income
from .serializers import IncomeSerializer
from django.http import Http404
from django.db.models import Sum

class getIncome(APIView):
    """
    List all income entries.
    """

    def get(self, request, format=None):
        income_entries = Income.objects.all()
        serializer = IncomeSerializer(income_entries, many=True)
        return Response(serializer.data)


class createIncome(APIView):
    """
    Create a new income entry.
    """

    def post(self, request, format=None):
        serializer = IncomeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class deleteIncome(APIView):
    """
    Delete a specific income entry.
    """

    def delete(self, request, pk, format=None):
        income = self.get_object(pk)
        income.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return Income.objects.get(pk=pk)
        except Income.DoesNotExist:
            raise Http404

class TotalIncome(APIView):
    def get(self, request, format=None):
        total_income = Income.objects.aggregate(total=Sum('amount'))
        return Response({'total_income': total_income['total']})
