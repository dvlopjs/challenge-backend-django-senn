from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from employees.employees_excel import get_excel_employees
from employees.serializers import EmployeeSerializer
from employees.services import create_employee, update_employee
from employees.selectors import list_employees, get_employees
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
    def put(self, request, id_employee):
        name = request.data.get('name')
        job_title = request.data.get('job_title')
        salary = request.data.get('salary')
        
        employee = update_employee(id_employee, name, job_title, salary)

        return Response(f"Employee {id_employee} updated successfully", status=201)

class ListEmployees(APIView):
    def get(self, request):
        query_job_or_name = request.query_params.get("query_job_or_name")
        filter_by_salary = request.query_params.get("filter_by_salary")

        employees = list_employees(query_job_or_name, filter_by_salary)
        
        return Response({"employees": EmployeeSerializer(employees, many=True).data}, status=200)

class ListReportSalary(APIView):
    def get(self, request):
        employees = get_employees()
        
        return get_excel_employees(employees)
        # return Response({"employees": EmployeeSerializer(employees, many=True).data}, status=200)

