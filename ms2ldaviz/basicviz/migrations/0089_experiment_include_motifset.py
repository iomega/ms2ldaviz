# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-02-19 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicviz', '0088_auto_20190218_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='include_motifset',
            field=models.TextField(null=True),
        ),
    ]
