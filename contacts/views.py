from django.shortcuts import render
from django.views import View 
from .models import Request
from .forms import RequestForm
from django.http import JsonResponse
from notifications.tasks import send_telegram_message_for_all_task
from home.models import Technology 
from contacts.models import (
    Worker, 
    CompanyStat,
)



class AboutView(View): 
    template_name = 'contacts/about.html'

    def get(self, request): 
        workers = Worker.objects.all()
        technologies = Technology.objects.all()
        company_stats = CompanyStat.objects.all()
        context = {
            'workers': workers, 
            'technologies': technologies,
            'company_stats': company_stats,
        }
        return render(request, self.template_name, context)


class SaveRequestView(View): 
    def post(self, request): 
        form: RequestForm = RequestForm(request.POST) 
        if form.is_valid():
            try: 
                new_request: Request = form.save() 
                
                message = 'Новая заявка с сайта'
                message += f'\n\nИмя: {new_request.name}\nТелефон: {new_request.phone}' 
                if new_request.message: 
                    message += f'\nСообщение: {new_request.message}'

                send_telegram_message_for_all_task.delay(message=message)


            except Exception as e: 
                print('Ошибка при сохранении заявки')

            return JsonResponse({'status': 'ok'}, status=200)
        print(form.errors)
        return JsonResponse({'status': 'error'}, status=400)