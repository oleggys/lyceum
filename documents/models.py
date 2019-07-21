import os

from django.db import models

# Create your models here.


class other_document(models.Model):
    class Meta():
        verbose_name_plural = "Другие документы"
    document = models.FileField(upload_to='documents/other')

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)

class charter_document(models.Model):
    class Meta():
        verbose_name_plural = "Устав образовательной организации"

    document = models.FileField(upload_to='documents/charter')

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)


class certificate_document(models.Model):
    class Meta():
        verbose_name_plural = "Свидетельство о государственной аккредитации"

    document = models.FileField(upload_to='documents/certificate')

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)

class pred_org_document(models.Model):
    class Meta():
        verbose_name_plural = "Предписание органов осуществляющих государственный контроль в сфере образования"

    document = models.FileField(upload_to='documents/pred_org')

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)


class prokurat_document(models.Model):
    class Meta():
        verbose_name_plural = "Праворазъяснительные материалы прокуратуры города Йошкар - Олы"

    document = models.FileField(upload_to='documents/prokurat')

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)

class ruls_document(models.Model):
    class Meta():
        verbose_name_plural = "Правила внутреннего трудового распорядка"

    document = models.FileField(upload_to='documents/ruls')

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)


class order_document(models.Model):
    class Meta():
        verbose_name_plural = "Порядок формирования перечня образовательных организаций " \
                              "осуществляющих индивидуальный отбор обучающихся"

    document = models.FileField(upload_to='documents/order')

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)

class order_exec_document(models.Model):
    class Meta():
        verbose_name_plural = "Отчеты об исполнении предписаний органов, осуществляющих государственный " \
                              "контроль в сфере образования"

    document = models.FileField(upload_to='documents/order_exec')

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)

class provisions(models.Model):
    class Meta():
        verbose_name_plural = "Положения лицея"
    name = models.CharField(max_length=200, verbose_name="Название положения")

    def __str__(self):
        return self.name



class provision_document(models.Model):
    class Meta():
        verbose_name_plural = "Локальные нормативные акты"

    document = models.FileField(upload_to='documents/provision')
    provision = models.ForeignKey(provisions, verbose_name="Положение")

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)

class license_document(models.Model):
    class Meta():
        verbose_name_plural = "Лицензия на осуществление образовательной деятельности"

    document = models.FileField(upload_to='documents/license')

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)

class gos_document(models.Model):
    class Meta():
        verbose_name_plural = "Государственное задание"

    document = models.FileField(upload_to='documents/gos')

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)


class plat_documents(models.Model):
    class Meta():
        verbose_name_plural = "Документы о порядке оказания платных образовательных услуг"

    document = models.FileField(upload_to='documents/plat')

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)

class internal_document(models.Model):
    class Meta():
        verbose_name_plural = "Внутренние документы лицея"

    document = models.FileField(upload_to='documents/internal')
    provision = models.ForeignKey(provisions, blank=True, verbose_name="Положение")

    def __str__(self):
        return os.path.basename(self.document.name)

    def filename(self):
        return os.path.basename(self.document.name)