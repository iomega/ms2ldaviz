# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('decomposition', '0016_decomposition_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beta',
            name='experiment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basicviz.Experiment'),
        ),
    ]
