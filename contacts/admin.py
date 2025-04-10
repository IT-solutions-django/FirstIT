from django.contrib import admin
from .models import (
    Request,
    CompanyInfo,
    Worker,
    CompanyStat,
)


@admin.register(Request) 
class RequestAdmin(admin.ModelAdmin): 
    list_display = ['name', 'phone', 'message']


@admin.register(CompanyInfo) 
class CompanyInfoAdmin(admin.ModelAdmin): 
    list_display = ['__str__']


@admin.register(Worker) 
class WorkerAdmin(admin.ModelAdmin): 
    list_display = ['name', 'department', 'position']


@admin.register(CompanyStat) 
class CompanyStatAdmin(admin.ModelAdmin): 
    list_display = ['heading', 'heading_label', 'lower_label']