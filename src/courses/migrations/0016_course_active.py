# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-25 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20190124_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
