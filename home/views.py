from django.shortcuts import render
from django.views import View 
from contacts.forms import RequestForm
from .models import (
    CompanyService,
    Case,
    CompanyClient,
    Technology,
)
from contacts.models import Worker


class HomeView(View): 
    template_name = 'home/home.html' 

    def get(self, request): 
        request_form = RequestForm(request.GET)
        services = CompanyService.objects.all()
        cases = Case.objects.all()
        clients = CompanyClient.objects.all()
        technologies = Technology.objects.all()
        workers = Worker.objects.all()
        context = {
            'request_form': request_form,
            'services': services,
            'cases': cases,
            'clients': clients, 
            'technologies': technologies,
            'workers': workers,
            'is_home_page': True,
        }
        return render(request, self.template_name, context)
    

class Show404View(View): 
    template_name = '404.html' 

    def get(self, request): 
        return render(request, self.template_name)