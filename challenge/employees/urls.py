from django.urls import path
from employees.views import CreateEmployee, UpdateEmployee

urlpatterns=[
    path("create/", CreateEmployee.as_view()),
    path("update/<int:id_employee>", UpdateEmployee.as_view())
]