from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Bill
from .serializers import BillSerializer
from django.http import Http404

class getBills(APIView):
    """
    List all bills.
    """

    def get(self, request, format=None):
        bills = Bill.objects.all()
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data)

class deleteBill(APIView):
    """
    Delete a bill instance.
    """

    def delete(self, request, pk, format=None):
        try:
            bill = Bill.objects.get(pk=pk)
            bill.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Bill.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class createBill(APIView):
    """
    Create a new bill.
    """

    def post(self, request, format=None):
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class updateBillStatus(APIView):
    """
    Update the status of a bill.
    """

    def post(self, request, pk, new_status, format=None):
        try:
            bill = Bill.objects.get(pk=pk)
            if new_status in ['unpaid', 'paid']:
                bill.status = new_status
                bill.save()
                return Response({"message": "Status updated successfully."})
            else:
                return Response({"message": "Invalid status value. Use 'unpaid' or 'paid'."}, status=status.HTTP_400_BAD_REQUEST)
        except Bill.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)