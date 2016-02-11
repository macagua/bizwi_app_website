from .models import Employees
from .serializers import EmployeeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmployeeList(APIView):
    """
    List all employee, or create a new employee.
    """
    def get(self, request, format=None):
        employee = Employees.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        employee = EmployeeSerializer(data=request.data)
        if employee.is_valid():
            employee.save()
            return Response(employee.data, status=status.HTTP_201_CREATED)
        return Response(employee.errors, status=status.HTTP_400_BAD_REQUEST)

