from .models import Employees
from .serializers import EmployeeSerializer
from rest_framework import generics


# Employees
class EmployeeList(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


