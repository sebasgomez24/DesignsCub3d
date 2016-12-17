# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-13 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_remove_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='likes',
        ),
        migrations.AlterField(
            model_name='project',
            name='document',
            field=models.FileField(default=1, upload_to='project_files', verbose_name='document'),
            preserve_default=False,
        ),
    ]