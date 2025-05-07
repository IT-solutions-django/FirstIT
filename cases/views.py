from django.shortcuts import render, get_object_or_404
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

        category = request.GET.get('category')
        if category: 
            cases = cases.filter(category=category)

        context = {
            'cases': cases,
            'case_categories': case_categories,
            'category': int(category) if category else None, 
            'category_name': CaseCategory.objects.filter(pk=category).first().name if category else None
        }
        return render(request, self.template_name, context)
    

class CaseView(View): 
    template_name = 'cases/case.html' 

    def get(self, request, case_slug: str): 
        case_ = get_object_or_404(Case, slug=case_slug)
        context = {
            'case': case_,
        }
        return render(request, self.template_name, context)