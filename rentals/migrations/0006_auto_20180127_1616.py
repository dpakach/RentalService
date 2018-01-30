# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-27 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0005_auto_20180127_0324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='lng',
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=256),
        ),
        migrations.AlterField(
            model_name='rental',
            name='description',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
    ]