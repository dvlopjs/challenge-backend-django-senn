from django.urls import path
from employees.views import CreateEmployee, UpdateEmployee, ListEmployees, ListReportSalary

urlpatterns=[
    path("create/", CreateEmployee.as_view()),
    path("update/<int:id_employee>", UpdateEmployee.as_view()),
    path("list/", ListEmployees.as_view()),
    path("reports/salary", ListReportSalary.as_view())
]