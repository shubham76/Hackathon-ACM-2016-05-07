# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assgn_app', '0007_auto_20160404_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='professor',
            name='subject',
            field=models.ManyToManyField(to='assgn_app.Subject'),
        ),
    ]
