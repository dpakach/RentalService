# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-07 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0009_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='author',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='rental',
        ),
        migrations.AddField(
            model_name='rental',
            name='tag',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
