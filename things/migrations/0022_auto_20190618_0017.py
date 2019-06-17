# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-17 18:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('things', '0021_auto_20190617_1733'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'ordering': ('-rank', 'name')},
        ),
        migrations.AddField(
            model_name='actor',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='actor',
            unique_together=set([('owner', 'rank', 'gender')]),
        ),
    ]
