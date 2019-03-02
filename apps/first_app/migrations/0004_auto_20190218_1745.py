# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-19 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_remove_course_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='name',
        ),
        migrations.AddField(
            model_name='course',
            name='desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
    ]