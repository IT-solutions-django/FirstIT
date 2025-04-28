from django.db import models
from django.urls import reverse
from cases.models import CaseCategory


class CompanyService(models.Model): 
    name = models.CharField('Название', max_length=50) 
    heading = models.CharField('Заголовок', max_length=50)
    label = models.CharField('Надпись под заголовком', max_length=50)
    text = models.TextField('Текст', max_length=500) 

    class Meta: 
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Case(models.Model): 
    name = models.CharField('Название', max_length=80)
    photo = models.ImageField('Картинка', upload_to='cases/backgrounds/')
    logo = models.ImageField('Логотип', upload_to='cases/logos/')

    goal_screenshot = models.ImageField('Скришнот (блок "Цель")', upload_to='cases/screenshots/', null=True, blank=True) 
    tasks_screenshot = models.ImageField('Скришнот (блок "Задачи")', upload_to='cases/screenshots/', null=True, blank=True)
    solution_screenshot = models.ImageField('Скриншот (блок "Решение")', upload_to='cases/screenshots/', null=True, blank=True)
    result_screenshot = models.ImageField('Скриншот (блок "Результаты")', upload_to='cases/screenshots/', null=True, blank=True)

    mobile_screenshot = models.ImageField('Скриншот (мобильный)', upload_to='cases/screenshots/', null=True, blank=True)
    desktop_screenshot = models.ImageField('Скриншот (десктоп)', upload_to='cases/screenshots/', null=True, blank=True) 
    screenshot_3 = models.ImageField('Скриншот №3 (поле пока не используется)', upload_to='cases/screenshots/', null=True, blank=True)
    screenshot_4 = models.ImageField('Скриншот №4 (поле пока не используется)', upload_to='cases/screenshots/', null=True, blank=True)

    description = models.TextField('Информация о клиенте', max_length=1000) 
    goal = models.TextField('Цель', max_length=800) 
    tasks = models.TextField('Задачи', max_length=1000)  
    solution = models.TextField('Решение', max_length=1000) 

    link = models.URLField('Ссылка на сайт', max_length=200, null=True, blank=True)

    category = models.ForeignKey(verbose_name='Категория', to=CaseCategory, on_delete=models.CASCADE, null=True, blank=True)

    slug = models.SlugField('Слаг', max_length=50)

    class Meta: 
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self) -> str: 
        return reverse('cases:case', args=[self.slug])
    

class CaseStat(models.Model): 
    number = models.CharField('Показатель', help_text='Например, "200+"', max_length=8)
    label = models.CharField('Метрика', help_text='Например, "посещений в день"', max_length=20)

    class Meta: 
        verbose_name = 'Метрика'
        verbose_name_plural = 'Метрики'

    def __str__(self):
        return f'{self.number} {self.label}'


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