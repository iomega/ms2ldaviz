# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-16 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicviz', '0085_auto_20181016_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='featureinstance2sub',
            name='mz',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='featureinstance2sub',
            name='sub_type',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
