# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-09-05 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0016_auto_20180329_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsblogconfig',
            name='author_no_photo',
            field=models.BooleanField(default=True, help_text='Display "No photo" icon if the user does not have one.', verbose_name="'Display No-photo icon"),
        ),
    ]
