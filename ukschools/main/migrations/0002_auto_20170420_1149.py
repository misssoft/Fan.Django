# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='gender',
            field=models.CharField(choices=[('M', 'Mixed'), ('B', 'Boys'), ('G', 'Girls')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='school',
            name='ofsted',
            field=models.CharField(choices=[('1', 'Outstanding'), ('2', 'Good'), ('3', 'Requires improvement'), ('4', 'Inadequate')], max_length=1),
        ),
        migrations.AlterField(
            model_name='school',
            name='phase',
            field=models.CharField(choices=[('P', 'Primary'), ('S', 'Secondary'), ('A', '16 to 18')], max_length=1),
        ),
        migrations.AlterField(
            model_name='school',
            name='religious',
            field=models.CharField(choices=[('N', 'No religious character'), ('CE', 'Church of England'), ('CA', 'Roman Catholic'), ('Me', 'Methodist'), ('URC', 'United Reformed Church'), ('Q', 'Quaker'), ('Mo', 'Moravian'), ('Se', 'Seventh Day Adventist'), ('O', 'Other Christian'), ('Mu', 'Muslim'), ('H', 'Hindu'), ('B', 'Buddist'), ('J', 'Jewish'), ('Si', 'Sikh'), ('U', 'Unitarian'), ('Mul', 'Multifaith')], default='N', max_length=3),
        ),
        migrations.AlterField(
            model_name='school',
            name='type',
            field=models.CharField(choices=[('A', 'Academy'), ('M', 'Maintained school'), ('I', 'Independent school'), ('S', 'Special school'), ('C', 'College')], max_length=1),
        ),
    ]
