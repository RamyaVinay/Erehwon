# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-28 14:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_remove_callforaction_contributors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='callforaction',
            old_name='call_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='callforaction',
            name='call_label',
        ),
    ]
