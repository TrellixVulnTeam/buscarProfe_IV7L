# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-22 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0002_auto_20181022_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='type',
            field=models.CharField(max_length=10),
        ),
    ]
