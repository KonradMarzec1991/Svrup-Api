# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-25 19:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0021_auto_20190125_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='categor',
            new_name='category',
        ),
    ]