# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 08:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assgn_app', '0011_assignmentq_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmenta',
            name='id',
        ),
        migrations.AlterField(
            model_name='assignmenta',
            name='assgn_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='assgn_app.AssignmentQ'),
        ),
    ]
