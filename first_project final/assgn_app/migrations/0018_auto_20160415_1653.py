# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-15 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assgn_app', '0017_subject_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subj_name',
            field=models.CharField(max_length=30),
        ),
    ]
