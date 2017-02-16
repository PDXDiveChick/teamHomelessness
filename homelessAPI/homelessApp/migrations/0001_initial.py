# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 17:36
from __future__ import unicode_literals

import django.contrib.postgres.fields.ranges
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agehousecomposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', django.contrib.postgres.fields.ranges.IntegerRangeField(null=True)),
                ('householdtype', models.CharField(max_length=255)),
                ('sheltertype', models.CharField(max_length=255)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('page', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'agehousecomposition',
            },
        ),
        migrations.CreateModel(
            name='Disability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disabilitytype', models.CharField(blank=True, max_length=255, null=True)),
                ('sheltertype', models.CharField(max_length=255)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('page', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'disability',
            },
        ),
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ethnicity', models.CharField(blank=True, max_length=255, null=True)),
                ('sheltertype', models.CharField(max_length=255)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('page', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ethnicity',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=255)),
                ('agerange', models.CharField(blank=True, max_length=255, null=True)),
                ('sheltertype', models.CharField(max_length=255)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('page', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'gender',
            },
        ),
        migrations.CreateModel(
            name='Geographiclocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geographiclocation', models.CharField(max_length=255)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('page', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'geographiclocation',
            },
        ),
        migrations.CreateModel(
            name='Homelessindividuals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheltertype', models.CharField(max_length=255)),
                ('age', models.CharField(blank=True, max_length=255, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('page', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'homelessindividuals',
            },
        ),
        migrations.CreateModel(
            name='Veterans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veteran', models.CharField(blank=True, max_length=255, null=True)),
                ('sheltertype', models.CharField(max_length=255)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('page', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'veterans',
            },
        ),
    ]