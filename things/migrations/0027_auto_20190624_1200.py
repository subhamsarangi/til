# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-24 06:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('things', '0026_auto_20190624_1156'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='actor',
            unique_together=set([('owner', 'rank', 'gender')]),
        ),
    ]
