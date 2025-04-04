from django.contrib import admin
from .models import (
    Request,
    CompanyInfo,
)


@admin.register(Request) 
class RequestAdmin(admin.ModelAdmin): 
    list_display = ['name', 'phone', 'message']


@admin.register(CompanyInfo) 
class CompanyInfoAdmin(admin.ModelAdmin): 
    list_display = ['__str__']