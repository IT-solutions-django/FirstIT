from django.shortcuts import render
from django.views import View 
from contacts.forms import RequestForm


class HomeView(View): 
    template_name = 'home/home.html' 

    def get(self, request): 
        request_form = RequestForm(request.GET)
        context = {
            'request_form': request_form,
        }
        return render(request, self.template_name, context)