from django.db import models


class CompanyService(models.Model): 
    name = models.CharField('Название', max_length=50) 
    heading = models.CharField('Заголовок', max_length=50)
    label = models.CharField('Надпись под заголовком', max_length=50)
    text = models.TextField('Текст', max_length=500) 

    class Meta: 
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Case(models.Model): 
    photo = models.ImageField('Картинка', upload_to='cases/backgrounds/')
    logo = models.ImageField('Логотип', upload_to='cases/logos/')

    class Meta: 
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'


class CompanyClient(models.Model): 
    logo = models.ImageField('Логотип', upload_to='clients') 

    class Meta: 
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Technology(models.Model): 
    name = models.CharField('Название', max_length=50) 
    description = models.TextField('Описание', max_length=500)
    is_highlighted = models.BooleanField('Выделена', default=False)

    class Meta: 
        verbose_name = 'Технология'
        verbose_name_plural = 'Технологии'