# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-26 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20180226_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='my location default', max_length=130),
        ),
    ]