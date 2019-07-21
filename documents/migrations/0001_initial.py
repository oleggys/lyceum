# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-06 09:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='certificate_document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/certificate')),
            ],
            options={
                'verbose_name_plural': 'Свидетельство о государственной аккредитации',
            },
        ),
        migrations.CreateModel(
            name='charter_document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/charter')),
            ],
            options={
                'verbose_name_plural': 'Устав образовательной организации',
            },
        ),
        migrations.CreateModel(
            name='gos_document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/gos')),
            ],
            options={
                'verbose_name_plural': 'Государственное задание',
            },
        ),
        migrations.CreateModel(
            name='internal_document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/internal')),
            ],
            options={
                'verbose_name_plural': 'Внутренние документы лицея',
            },
        ),
        migrations.CreateModel(
            name='license_document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/license')),
            ],
            options={
                'verbose_name_plural': 'Лицензия на осуществление образовательной деятельности',
            },
        ),
        migrations.CreateModel(
            name='order_document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/order')),
            ],
            options={
                'verbose_name_plural': 'Порядок формирования перечня образовательных организаций осуществляющих индивидуальный отбор обучающихся',
            },
        ),
        migrations.CreateModel(
            name='order_exec_document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/order_exec')),
            ],
            options={
                'verbose_name_plural': 'Отчеты об исполнении предписаний органов, осуществляющих государственный контроль в сфере образования',
            },
        ),
        migrations.CreateModel(
            name='other_document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/other')),
            ],
            options={
                'verbose_name_plural': 'Другие документы',
            },
        ),
        migrations.CreateModel(
            name='plat_documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/plat')),
            ],
            options={
                'verbose_name_plural': 'Документы о порядке оказания платных образовательных услуг',
            },
        ),
        migrations.CreateModel(
            name='pred_org_document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/pred_org')),
            ],
            options={
                'verbose_name_plural': 'Предписание органов осуществляющих государственный контроль в сфере образования',
            },
        ),
        migrations.CreateModel(
            name='prokurat_document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/prokurat')),
            ],
            options={
                'verbose_name_plural': 'Праворазъяснительные материалы прокуратуры города Йошкар - Олы',
            },
        ),
        migrations.CreateModel(
            name='provision_document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/provision')),
            ],
            options={
                'verbose_name_plural': 'Локальные нормативные акты',
            },
        ),
        migrations.CreateModel(
            name='provisions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название положения')),
            ],
            options={
                'verbose_name_plural': 'Положения лицея',
            },
        ),
        migrations.CreateModel(
            name='ruls_document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/ruls')),
            ],
            options={
                'verbose_name_plural': 'Правила внутреннего трудового распорядка',
            },
        ),
        migrations.AddField(
            model_name='provision_document',
            name='provision',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.provisions', verbose_name='Положение'),
        ),
        migrations.AddField(
            model_name='internal_document',
            name='provision',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='documents.provisions', verbose_name='Положение'),
        ),
    ]
