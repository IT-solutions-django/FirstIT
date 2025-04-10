from django.contrib import admin
from .models import CaseCategory


@admin.register(CaseCategory)
class CaseCategoryAdmin(admin.ModelAdmin): 
    list_display = ['name']
