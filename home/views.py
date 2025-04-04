from django.shortcuts import render
from django.views import View 
from contacts.forms import RequestForm
from .models import (
    CompanyService,
    Case,
    CompanyClient,
    Technology,
)


class HomeView(View): 
    template_name = 'home/home.html' 

    def get(self, request): 
        request_form = RequestForm(request.GET)
        services = CompanyService.objects.all()
        cases = Case.objects.all()
        clients = CompanyClient.objects.all()
        technologies = Technology.objects.all()
        context = {
            'request_form': request_form,
            'services': services,
            'cases': cases,
            'clients': clients, 
            'technologies': technologies,
        }
        return render(request, self.template_name, context)