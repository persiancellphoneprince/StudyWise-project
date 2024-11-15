from django.db import models
from pytils.translit import slugify
from datetime import datetime

class Subject(models.Model):
    name = models.CharField("Название предмета", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Offer(models.Model):

    title = models.CharField("Название предложения", max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Выберите предмет")
    teacher = models.CharField("Имя преподователя", max_length=100)
    experience = models.CharField("Опыт", max_length =50, default="Без опыта")
    payment = models.CharField("Стоимость", max_length=50)
    description = models.TextField("Описание предложения")
    address = models.CharField("Адрес", max_length=100)
    phone = models.CharField("Телефон", max_length=14)
    agency = models.CharField("Агентство", max_length=80, default="Самозанятый репетитор")
    created_at = models.DateTimeField("Дата и время публикации", default = datetime.now)

    class Meta:
        verbose_name = "Предложение"
        verbose_name_plural = "Предложения"

    def __str__(self):
        return self.title

class AllSubjects(models.Model):    
    title = models.CharField("Предмет", max_length=50)

class Favourite(models.Model):
    title = models.CharField("Заголовок", max_length=80)
    teacher = models.CharField("Имя преподователя", max_length=100)
    experience = models.CharField("Опыт", max_length =50, default="Без опыта")
    payment = models.CharField("Стоимость", max_length=50)
    description = models.TextField("Описание предложения", default = "Описание не предоставлено")  # Добавил описание, чтобы его можно было вывести
    phone = models.CharField("Телефон", max_length=14, default='')  # Для отображения на странице
    address = models.CharField("Адрес", max_length=100,default="Онлайн")  # Для отображения на странице
    agency = models.CharField("Агентство", max_length=80, default="Самозанятый репетитор")
    created_at = models.DateTimeField("Дата и время публикации", default=datetime.now)

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"

    def __str__(self):
        return self.title
    

