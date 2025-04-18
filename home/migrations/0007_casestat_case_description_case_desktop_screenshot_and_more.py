# Generated by Django 5.1.7 on 2025-04-10 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_technology_is_highlighted'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(help_text='Например, "200+"', max_length=8, verbose_name='Показатель')),
                ('label', models.CharField(help_text='Например, "посещений в день"', max_length=20, verbose_name='Метрика')),
            ],
            options={
                'verbose_name': 'Метрика',
                'verbose_name_plural': 'Метрики',
            },
        ),
        migrations.AddField(
            model_name='case',
            name='description',
            field=models.TextField(default='', max_length=1000, verbose_name='Информация о клиенте'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='desktop_screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='cases/screenshots/', verbose_name='Скриншот №2 (десктоп)'),
        ),
        migrations.AddField(
            model_name='case',
            name='goal',
            field=models.TextField(default='', max_length=800, verbose_name='Цель'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='goal_screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='cases/screenshots/', verbose_name='Скришнот (блок "Цель")'),
        ),
        migrations.AddField(
            model_name='case',
            name='mobile_screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='cases/screenshots/', verbose_name='Скриншот №1 (мобильный)'),
        ),
        migrations.AddField(
            model_name='case',
            name='name',
            field=models.CharField(default='', max_length=80, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='result',
            field=models.TextField(default='', max_length=1000, verbose_name='Результат'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='screenshot_3',
            field=models.ImageField(blank=True, null=True, upload_to='cases/screenshots/', verbose_name='Скриншот №3'),
        ),
        migrations.AddField(
            model_name='case',
            name='screenshot_4',
            field=models.ImageField(blank=True, null=True, upload_to='cases/screenshots/', verbose_name='Скриншот №4'),
        ),
        migrations.AddField(
            model_name='case',
            name='slug',
            field=models.SlugField(default='', verbose_name='Слаг'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='solution',
            field=models.TextField(default='', max_length=1000, verbose_name='Решение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='solution_screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='cases/screenshots/', verbose_name='Скриншот (блок "Решение")'),
        ),
        migrations.AddField(
            model_name='case',
            name='tasks',
            field=models.TextField(default='', max_length=1000, verbose_name='Задачи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='tasks_screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='cases/screenshots/', verbose_name='Скришнот (блок "Задачи")'),
        ),
    ]
