# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 07:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WMMessage', '0004_auto_20171019_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wmmessage',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
