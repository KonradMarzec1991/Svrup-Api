# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-23 22:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20190123_2224'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lecture',
            unique_together=set([('slug', 'course')]),
        ),
    ]
