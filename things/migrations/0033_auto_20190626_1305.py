# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-26 07:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0032_auto_20190626_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, validators=[django.core.validators.RegexValidator("^[a-zA-Z0-9 %&#?!();.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, validators=[django.core.validators.RegexValidator("^[a-zA-Z0-9 %&#?!();.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='anime',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator("^[a-zA-Z0-9 %&#?!();.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")]),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator("^[a-zA-Z0-9 %&#?!();.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")]),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator("^[a-zA-Z0-9 %&#?!();.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")]),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator("^[a-zA-Z0-9 %&#?!();.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator("^[a-zA-Z0-9 %&#?!();.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")]),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator("^[a-zA-Z0-9 %&#?!();.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")]),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=80, validators=[django.core.validators.RegexValidator("^[a-zA-Z0-9 %&#?!();.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")]),
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator("^[a-zA-Z0-9 %&#?!();.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator("^[a-zA-Z0-9 %&#?!();.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")]),
        ),
        migrations.AlterField(
            model_name='website',
            name='name',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator("^[a-zA-Z0-9 %&#?!();.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")]),
        ),
        migrations.AlterField(
            model_name='youtubechannel',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator("^[a-zA-Z0-9 %&#?!();.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")]),
        ),
    ]
