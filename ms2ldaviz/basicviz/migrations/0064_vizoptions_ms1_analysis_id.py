# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicviz', '0063_mass2motif_linkmotif'),
    ]

    operations = [
        migrations.AddField(
            model_name='vizoptions',
            name='ms1_analysis_id',
            field=models.IntegerField(null=True),
        ),
    ]
