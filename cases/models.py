from django.db import models


class CaseCategory(models.Model): 
    name = models.CharField('Название', max_length=50) 

    class Meta: 
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self): 
        return f'{self.name}'
    


class CaseMetric(models.Model): 
    number = models.CharField('Название', max_length=50) 
    label = models.CharField('Подпись', max_length=50) 
    case = models.ForeignKey('home.Case', on_delete=models.CASCADE, related_name='metrics')


    class Meta: 
        verbose_name = 'Метрика'
        verbose_name_plural = 'Метрики'
