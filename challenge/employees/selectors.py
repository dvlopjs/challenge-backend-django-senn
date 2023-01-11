from employees.models import Employee
from django.db.models import Q
from employees.filters import name_or_job_name_contains, salary_contains


def get_employee(id):
    employee = Employee.objects.get(id=id)
    return employee

def list_employees(query_job_or_name, filter_by_salary):
    return Employee.objects.filter(
        (name_or_job_name_contains(query_job_or_name))
        &
        Q(salary_contains(filter_by_salary))
    )

def get_employees():
    return Employee.objects.all()