from django.db.models import Q

def name_or_job_name_contains(query_job_or_name):
    return Q(name__icontains=query_job_or_name) | Q(job_title__icontains=query_job_or_name)

def salary_contains(filter_by_salary):
    return Q(salary__icontains=filter_by_salary)