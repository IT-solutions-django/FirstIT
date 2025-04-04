from django.shortcuts import render
from django.views import View 
from .models import Request
from .forms import RequestForm
from django.http import JsonResponse
from notifications.tasks import send_telegram_message_for_all_task


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