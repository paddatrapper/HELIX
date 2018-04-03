# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-22 21:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0078_auto_20180305_1157'),
        ('helix', '0003_helixgreenassessmentproperty_reference_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='HELIXGreenAssessment',
            fields=[
                ('greenassessment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='seed.GreenAssessment')),
                ('is_reso_certification', models.BooleanField(default=True)),
            ],
            bases=('seed.greenassessment',),
        ),
    ]
