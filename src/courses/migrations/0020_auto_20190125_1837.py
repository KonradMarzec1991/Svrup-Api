# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-25 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_auto_20190125_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('main', 'Main'), ('sec', 'Secondary')], default='main', max_length=120),
        ),
    ]