# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-23 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0044_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='grupo_usuario',
        ),
        migrations.AlterField(
            model_name='autor',
            name='username',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nome de Usuário'),
        ),
    ]
