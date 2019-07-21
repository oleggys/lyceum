import datetime

from django.db import models

# Create your models here.


class offer(models.Model):
    class Meta():
        verbose_name_plural = "Предложения"

    name = models.CharField(max_length=60, verbose_name="Имя")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=11, verbose_name="Телефон")
    topic = models.CharField(max_length=30, verbose_name="Тема")
    text = models.TextField(verbose_name="Предложение")
    pub_date = models.DateTimeField(default=datetime.datetime.now())


class complaint(models.Model):
    class Meta():
        verbose_name_plural = "Жалобы"

    name = models.CharField(max_length=60, verbose_name="Имя")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=11, verbose_name="Телефон")
    topic = models.CharField(max_length=30, verbose_name="Тема")
    text = models.TextField(verbose_name="Жалоба")
    pub_date = models.DateTimeField(default=datetime.datetime.now())