# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 20:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WMMessage', '0003_auto_20171019_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wmmessage',
            old_name='msg_content',
            new_name='message',
        ),
    ]
