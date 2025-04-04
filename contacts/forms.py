from django import forms 
from .models import Request


class RequestForm(forms.ModelForm): 
    class Meta:
        model = Request
        fields = ['name', 'phone', 'message']
        labels = {
            'name': 'Имя',
            'phone': 'Телефон',
            'message': 'Сообщение'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ваше имя',
            }),
            'phone': forms.TextInput(attrs={
                'type': 'tel', 
                'placeholder': '+7',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Кратко опишите свой вопрос',
                'rows': 3,
            })
        }