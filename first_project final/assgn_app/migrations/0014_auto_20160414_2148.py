# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assgn_app', '0013_auto_20160413_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentq',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assignmentq',
            name='assgn_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='assignmentq',
            unique_together=set([('assgn_id', 'subj_id')]),
        ),
    ]