# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-21 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20170517_2335'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AddField(
            model_name='callforaction',
            name='call_label',
            field=models.CharField(choices=[(b'A', b'Activism'), (b'DA', b'Digital Activism'), (b'CD', b'Community Development'), (b'UP', b'Urban Planning'), (b'NE', b'New Ecologies'), (b'AE', b'Alternative Economies'), (b'CM', b'Citizen Movement'), (b'AI', b'Artistic Interventions')], default=b'A', max_length=30),
        ),
        migrations.AddField(
            model_name='idea',
            name='label',
            field=models.CharField(choices=[(b'A', b'Activism'), (b'DA', b'Digital Activism'), (b'CD', b'Community Development'), (b'UP', b'Urban Planning'), (b'NE', b'New Ecologies'), (b'AE', b'Alternative Economies'), (b'CM', b'Citizen Movement'), (b'AI', b'Artistic Interventions')], default=b'A', max_length=30),
        ),
        migrations.AddField(
            model_name='project',
            name='label',
            field=models.CharField(choices=[(b'A', b'Activism'), (b'DA', b'Digital Activism'), (b'CD', b'Community Development'), (b'UP', b'Urban Planning'), (b'NE', b'New Ecologies'), (b'AE', b'Alternative Economies'), (b'CM', b'Citizen Movement'), (b'AI', b'Artistic Interventions')], default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='project',
            name='material',
            field=models.URLField(blank=True, max_length=300),
        ),
    ]
