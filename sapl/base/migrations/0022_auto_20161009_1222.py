# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-09 15:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('base', '0021_auto_20161006_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('nome', models.CharField(blank=True, max_length=50, verbose_name='Autor')),
                ('cargo', models.CharField(blank=True, max_length=50)),
                ('content_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='TipoAutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('content_type', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Modelo do Tipo de Autor')),
            ],
            options={
                'verbose_name': 'Tipo de Autor',
                'verbose_name_plural': 'Tipos de Autor',
            },
        ),
        migrations.AddField(
            model_name='autor',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.TipoAutor', verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='autor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
