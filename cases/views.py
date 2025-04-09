from django.shortcuts import render
from django.views import View 
from home.models import Case


class CasesView(View): 
    template_name = 'cases/cases.html'

    def get(self, request): 
        cases = Case.objects.all()
        context = {
            'cases': cases,
        }
        return render(request, self.template_name, context)