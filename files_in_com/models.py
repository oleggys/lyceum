import datetime
import os

from django.db import models
from lyceum.models import subject
# Create your models here.


class codifier(models.Model):
    class Meta():
        verbose_name_plural = u"Кодификаторы"
    document = models.FileField(upload_to='codifiers')
    subject = models.ForeignKey(subject, verbose_name="Предмет")

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)


class training_file(models.Model):
    class Meta():
        verbose_name_plural = u"Тренировочные задания"
    document = models.FileField(upload_to='training')
    subject = models.ForeignKey(subject, verbose_name="Предмет")

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)

    def shot_text(self):
        if len(self.filename()) > 50:
            return self.filename()[:50] + "..."
        else:
            return self.filename()


class result(models.Model):
    class Meta():
        verbose_name_plural = u"Результаты тестирования"
    document = models.FileField(upload_to='results')
    subject = models.ForeignKey(subject, verbose_name="Предмет")

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)

    def shot_text(self):
        if len(self.filename()) > 50:
            return self.filename()[:50] + "..."
        else:
            return self.filename()

class dis_learning(models.Model):
    class Meta():
        verbose_name_plural = u"Дистанционное обучение"
    document = models.FileField(upload_to='dis_learning')
    subject = models.ForeignKey(subject, verbose_name="Предмет")
    year = models.DateField(blank=True, null=True, default=datetime.datetime.now(), verbose_name="Год")

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)

    def shot_text(self):
        if len(self.filename()) > 50:
            return self.filename()[:50] + "..."
        else:
            return self.filename()


class other(models.Model):
    class Meta():
        verbose_name_plural = u"Другие"
    document = models.FileField(upload_to='other')

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)

    def shot_text(self):
        if len(self.filename()) > 23:
            return self.filename()[:23] + "..."
        else:
            return self.filename()