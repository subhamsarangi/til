# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-19 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0023_auto_20190618_0026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='adultmodel',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='anime',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='dancer',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='director',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='femalemodel',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='fitnessperson',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='musician',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='sportsperson',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='tvshow',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='vehicle',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='website',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='writer',
            options={'ordering': ('rank', 'name')},
        ),
        migrations.AlterModelOptions(
            name='youtubechannel',
            options={'ordering': ('rank', 'name')},
        ),
    ]
