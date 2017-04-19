# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phase', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('ofsted', models.CharField(max_length=50)),
                ('ofstedInspected', models.DateTimeField()),
                ('religious', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=10)),
            ],
        ),
    ]
