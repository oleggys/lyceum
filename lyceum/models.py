import datetime

from django.db import models


# Create your models here.
class subject(models.Model):
    class Meta():
        verbose_name_plural = u"Предметы"
    subject_name = models.CharField(max_length=20, verbose_name="Название предмета")

    def __str__(self):
        return self.subject_name

    def shot_text(self):
        if len(self.subject_name) > 5:
            return self.subject_name[:5]
        else:
            return self.subject_name


class positions(models.Model):
    class Meta():
        verbose_name_plural = u"Должности"
    position_name = models.CharField(max_length=50, verbose_name="Должность")

    def __str__(self):
        return self.position_name



class Staff(models.Model):
    class Meta():
        db_table = 'Staff'
        verbose_name_plural = u"Коллектив"
    avatar = models.ImageField(upload_to='img', verbose_name="Изображение", default="avatar.png")
    name = models.CharField(max_length=12, verbose_name="Имя")
    surname = models.CharField(max_length=25, verbose_name="Фамилия")
    last_name = models.CharField(max_length=25, verbose_name="Отчество")
    education = models.TextField(verbose_name="Образование")
    administration = models.BooleanField(default=False, verbose_name="Находится в администрации лицея")
    position = models.ManyToManyField(positions, verbose_name="Должность")
    subjects = models.ManyToManyField(subject, blank=True, verbose_name="Преподаёт")

    def __str__(self):
        return self.name

class Lyceum_news(models.Model):
    class Meta():
        db_table = 'News'
        verbose_name_plural = u"Новости"
    name = models.CharField(max_length=250, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст новости")
    pub_date = models.DateTimeField(default=datetime.datetime.now(), verbose_name="Дата и время публикации")

    def __str__(self):
        return self.name



class Event(models.Model):
    class Meta():
        db_table = 'Events'
        verbose_name_plural = u"События для календаря"
    event_date = models.DateField(verbose_name="Дата события")

    def __str__(self):
        return str(self.event_date)


class events_in_day(models.Model):
    event_begin_time = models.TimeField(verbose_name="Время начала")
    event_end_time = models.TimeField(verbose_name="Время окончания", blank=True, null=True)
    event_name = models.CharField(max_length=250, verbose_name="Название мероприятия")
    event_day = models.ForeignKey(Event)

    def __str__(self):
        return self.event_name

class message(models.Model):
    class Meta():
        db_table = 'messages'
        verbose_name_plural = u"Сообщения"
    email = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    topic = models.CharField(max_length=40)
    text = models.TextField()

    def __str__(self):
        return self.email