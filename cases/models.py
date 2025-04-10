from django.db import models


class CaseCategory(models.Model): 
    name = models.CharField('Название', max_length=50) 

    class Meta: 
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self): 
        return f'{self.name}'