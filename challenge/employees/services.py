from employees.models import Employee
from employees.selectors import get_employee

def create_employee(*, name, job_title, salary):
    employee = Employee.objects.create(
        name=name,
        job_title=job_title,
        salary=salary
    )
    return employee

def update_employee(id_employee, name, job_title, salary):
    employee = get_employee(id_employee)
    employee.name = name
    employee.job_title = job_title
    employee.salary = salary

    employee.save()
    return employee