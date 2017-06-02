# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-21 21:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20170521_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
