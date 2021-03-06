# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assgn_app', '0008_auto_20160404_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assgn_a_file', models.FileField(upload_to='temp.pdf')),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentQ',
            fields=[
                ('assgn_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('assgn_q_file', models.FileField(upload_to='temp.pdf')),
            ],
        ),
        migrations.CreateModel(
            name='StudSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.RemoveField(
            model_name='professorlogin',
            name='unique_id',
        ),
        migrations.RemoveField(
            model_name='studentlogin',
            name='unique_id',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='course',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='unique_id',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='id',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='name',
        ),
        migrations.AddField(
            model_name='professor',
            name='password',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professor',
            name='prof_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='prof_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='assgn_app.Professor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='subj_id',
            field=models.CharField(default=0, max_length=20, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='subj_name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProfessorLogin',
        ),
        migrations.DeleteModel(
            name='StudentLogin',
        ),
        migrations.AddField(
            model_name='studsub',
            name='stud_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assgn_app.Student'),
        ),
        migrations.AddField(
            model_name='studsub',
            name='subj_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assgn_app.Subject'),
        ),
        migrations.AddField(
            model_name='assignmentq',
            name='subj_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assgn_app.Subject'),
        ),
        migrations.AddField(
            model_name='assignmenta',
            name='assgn_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assgn_app.AssignmentQ'),
        ),
        migrations.AddField(
            model_name='assignmenta',
            name='unique_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assgn_app.Student'),
        ),
    ]
