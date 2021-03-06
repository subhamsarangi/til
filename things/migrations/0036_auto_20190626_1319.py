# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-26 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0035_auto_20190626_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='watch_status',
            field=models.CharField(choices=[('h', 'Waiting For Next Release'), ('w', 'Completed'), ('s', 'Started Watching'), ('n', 'Wish to Watch')], max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='watch_status',
            field=models.CharField(choices=[('h', 'Waiting For Next Release'), ('w', 'Completed'), ('s', 'Started Watching'), ('n', 'Wish to Watch')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='watch_status',
            field=models.CharField(choices=[('h', 'Waiting For Next Release'), ('w', 'Completed'), ('s', 'Started Watching'), ('n', 'Wish to Watch')], max_length=20, null=True),
        ),
    ]
