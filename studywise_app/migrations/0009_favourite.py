# Generated by Django 5.1.3 on 2024-11-15 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studywise_app', '0008_allsubjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Заголовок')),
                ('teacher', models.CharField(max_length=100, verbose_name='Имя преподователя')),
                ('experience', models.CharField(default='Без опыта', max_length=50, verbose_name='Опыт')),
                ('payment', models.CharField(max_length=50, verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранные',
            },
        ),
    ]
