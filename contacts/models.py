from django.db import models


class Request(models.Model): 
    name = models.CharField('Имя', max_length=80)
    phone = models.CharField('Номер телефона', max_length=18)
    message = models.TextField('Сообщение', max_length=400, null=True, blank=True) 

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'