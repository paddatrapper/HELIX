# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-08 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helix', '0002_helixorganization'),
    ]

    operations = [
        migrations.AddField(
            model_name='helixgreenassessmentproperty',
            name='reference_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]