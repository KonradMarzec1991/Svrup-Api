# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-25 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_auto_20190123_2038'),
        ('category', '0003_category_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='videos.Video'),
        ),
    ]
