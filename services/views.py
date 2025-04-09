from django.shortcuts import render
from django.views import View 
from home.models import CompanyService


class ServicesView(View): 
    template_name = 'services/services.html' 

    def get(self, request): 
        services = CompanyService.objects.all()
        context = {
            'services': services,
        }
        return render(request, self.template_name, context)