from django.contrib import admin
from .models import (
    CompanyService, 
    Case,
    CompanyClient,
    Technology,
)
from cases.models import CaseMetric


class CaseMetricInline(admin.TabularInline):
    model = CaseMetric
    extra = 1


@admin.register(CompanyService) 
class CompanyServiceAdmin(admin.ModelAdmin): 
    list_display = ['name']


@admin.register(Case) 
class CaseAdmin(admin.ModelAdmin): 
    list_display = ['name', 'photo', 'logo']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CaseMetricInline]


@admin.register(CompanyClient) 
class CompanyClientAdmin(admin.ModelAdmin): 
    list_display = ['pk', 'logo']


@admin.register(Technology) 
class TechnologyAdmin(admin.ModelAdmin): 
    list_display = ['name']