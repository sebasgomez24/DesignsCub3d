# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-03 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20161213_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='note',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
