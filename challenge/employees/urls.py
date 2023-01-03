from django.urls import path
from employees.views import CreateEmployee

urlpatterns=[
    path("create/", CreateEmployee.as_view())
]