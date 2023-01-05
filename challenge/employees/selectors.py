from employees.models import Employee

def get_employee(id):
    employee = Employee.objects.get(id=id)
    return employee