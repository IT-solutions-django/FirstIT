from django.shortcuts import render
from django.views import View 
from home.models import (
    Case, 
)
from .models import (
    CaseCategory,
)


class CasesView(View): 
    template_name = 'cases/cases.html'

    def get(self, request): 
        cases = Case.objects.all()
        case_categories = CaseCategory.objects.all()
        context = {
            'cases': cases,
            'case_categories': case_categories,
        }
        return render(request, self.template_name, context)