# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assgn_app', '0014_auto_20160414_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentq',
            name='id',
        ),
        migrations.AlterField(
            model_name='assignmentq',
            name='assgn_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
