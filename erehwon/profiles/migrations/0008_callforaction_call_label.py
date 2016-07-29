# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-27 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_callforaction_contributors'),
    ]

    operations = [
        migrations.AddField(
            model_name='callforaction',
            name='call_label',
            field=models.CharField(choices=[(b'A', b'Activism'), (b'DA', b'Digital Activism'), (b'CD', b'Community Development'), (b'UP', b'Urban Planning'), (b'NE', b'New Ecologies'), (b'AE', b'Alternative Economies'), (b'CM', b'Citizen Movement'), (b'AI', b'Artistic Interventions')], default=b'A', max_length=30),
        ),
    ]
