from employees.models import Employee

def create_employee(*, name, job_title, salary):
    employee = Employee.objects.create(
        name=name,
        job_title=job_title,
        salary=salary
    )
    return employee

def update_employee(id, name, job_title, salary):
    employee = Employee.objects.get(id=id)