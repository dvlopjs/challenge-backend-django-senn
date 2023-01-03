from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from employees.services import create_employee, update_employee
# Create your views here.
class CreateEmployee(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        job_title = serializers.CharField()
        salary = serializers.DecimalField(max_digits=15, decimal_places=2)
    
    def post(self, request):
        _serializer = self.InputSerializer(data=request.data)
        _serializer.is_valid(raise_exception=True)

        employee = create_employee(**_serializer.validated_data)
        return Response(f"Employee {employee.name} created successfully", status=201)

class UpdateEmployee(APIView):
    def put(self, response, employee_id):
        name = request.data.get('name')
        job_title = request.data.get('job_title')
        salary = request.data.get('salary')
        
        employee = update_employee(name, job_title, salary)