# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-28 07:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('decomposition', '0011_auto_20170221_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalMotifsToSets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decomposition.GlobalMotif')),
            ],
        ),
        migrations.CreateModel(
            name='MotifSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('featureset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decomposition.FeatureSet')),
            ],
        ),
        migrations.AddField(
            model_name='documentglobalmass2motif',
            name='decomposition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='decomposition.Decomposition'),
        ),
        migrations.AddField(
            model_name='globalmotifstosets',
            name='motifset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decomposition.MotifSet'),
        ),
        migrations.AddField(
            model_name='decomposition',
            name='motifset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='decomposition.MotifSet'),
        ),
    ]
