# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assgn_app', '0006_remove_assignment_stud_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='assgn_file',
            field=models.FileField(upload_to='temp.pdf'),
        ),
    ]
