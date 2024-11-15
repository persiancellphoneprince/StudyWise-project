# Generated by Django 5.1.3 on 2024-11-15 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studywise_app', '0009_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='favourite',
            name='address',
            field=models.CharField(default='Онлайн', max_length=100, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='agency',
            field=models.CharField(default='Самозанятый репетитор', max_length=80, verbose_name='Агентство'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время публикации'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='description',
            field=models.TextField(default='Описание не предоставлено', max_length=200, verbose_name='Описание предложения'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='phone',
            field=models.CharField(default='', max_length=14, verbose_name='Телефон'),
        ),
    ]
