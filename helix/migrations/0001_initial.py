# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-08-25 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seed', '0071_auto_20170721_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='HELIXGreenAssessment',
            fields=[
                ('greenassessment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='seed.GreenAssessment')),
                ('disclosure_default', models.TextField(max_length=100)),
            ],
            bases=('seed.greenassessment',),
        ),
        migrations.CreateModel(
            name='HELIXGreenAssessmentProperty',
            fields=[
                ('greenassessmentproperty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='seed.GreenAssessmentProperty')),
                ('disclosure', models.TextField(max_length=100)),
            ],
            bases=('seed.greenassessmentproperty',),
        ),
        migrations.CreateModel(
            name='HelixMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement_type', models.CharField(choices=[(b'PROD', b'Production'), (b'CONS', b'Consumption'), (b'COST', b'Cost'), (b'EMIT', b'Emissions')], max_length=4)),
                ('measurement_subtype', models.CharField(max_length=100)),
                ('fuel', models.CharField(choices=[(b'ELEC', b'Electric'), (b'NATG', b'Natural Gas'), (b'HEAT', b'Heating Oil'), (b'PROP', b'Propane'), (b'CWOOD', b'Cord Wood'), (b'PWOOD', b'Pellet Wood')], max_length=5)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('unit', models.CharField(choices=[(b'KWH', b'Kilowatt Hours'), (b'KW', b'Kilowatt'), (b'GAL', b'Gallon'), (b'MMBTU', b'mmbtu'), (b'TON', b'ton'), (b'LB', b'pound'), (b'CORD', b'cord'), (b'THERM', b'therm')], max_length=5)),
                ('status', models.CharField(choices=[(b'ACTUAL', b'Actual'), (b'ESTIMATE', b'Estimated'), (b'PART_ESTIMATE', b'Partially Estimated')], max_length=13)),
                ('assessment_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.GreenAssessmentProperty')),
            ],
        ),
    ]