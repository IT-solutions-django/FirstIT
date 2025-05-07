from django.db import models


class Request(models.Model): 
    name = models.CharField('Имя', max_length=80)
    phone = models.CharField('Номер телефона', max_length=18)
    message = models.TextField('Сообщение', max_length=400, null=True, blank=True) 

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class CompanyInfo(models.Model): 
    phone = models.CharField('Номер телефона', max_length=18)
    email = models.EmailField('Email', max_length=80) 
    address = models.CharField('Адрес', max_length=100) 

    whatsapp = models.URLField('Ссылка на WhatsApp', max_length=100) 
    telegram = models.URLField('Ссылка на Telegram', max_length=100) 
    vk = models.URLField('Ссылка на ВК', max_length=100)
    whatsapp = models.URLField('Ссылка на WhatsApp', max_length=100)
    github = models.URLField('Ссылка на Github', max_length=100)


    class Meta:
        verbose_name = 'Информация о компании'
        verbose_name_plural = 'Информация о компании'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls) -> "CompanyInfo":
        instance, created = cls.objects.get_or_create(id=1)
        return instance
    
    def __str__(self): 
        return f'Информация о компании'
    

class Worker(models.Model): 
    name = models.CharField('Имя', max_length=100) 
    department = models.CharField('Отдел', max_length=100)
    position = models.CharField('Должность', max_length=100) 
    photo = models.ImageField('Фото', upload_to='workers/', null=True, blank=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class CompanyStat(models.Model): 
    heading = models.CharField('Заголовок', max_length=40) 
    heading_label = models.CharField('Подпись у заголовка', max_length=40) 
    lower_label = models.CharField('Надпись снизу', max_length=55)

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'