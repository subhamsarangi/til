# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-13 19:20
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('things', '0007_movie_tvshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator("^[a-zA-Z0-9 %&#?!;.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")])),
                ('watch_status', models.CharField(choices=[('w', 'Watched'), ('n', 'Not watched'), ('s', 'Started'), ('h', 'Halfway through')], max_length=20)),
                ('anime_type', models.CharField(choices=[('s', 'Series'), ('m', 'Movie')], max_length=20)),
                ('rank', models.CharField(blank=True, choices=[('a', '1'), ('b', '2'), ('c', '3'), ('d', '4'), ('e', '5')], max_length=12, null=True)),
                ('poster', models.URLField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator("^[a-zA-Z0-9 %&#?!;.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")])),
                ('read_status', models.CharField(choices=[('rd', 'Read'), ('nr', 'Not read'), ('st', 'Started'), ('ht', 'Halfway through'), ('ad', 'Almost Done')], max_length=20)),
                ('source', models.CharField(choices=[('ph', 'I own a physical copy'), ('eb', 'I have an eBook'), ('lb', 'Got it at the Library'), ('br', 'Borrowed from someone'), ('wb', 'Reading it on a website')], max_length=40)),
                ('rank', models.CharField(blank=True, choices=[('a', '1'), ('b', '2'), ('c', '3'), ('d', '4'), ('e', '5')], max_length=12, null=True)),
                ('cover', models.URLField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator("^[a-zA-Z0-9 %&#?!;.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")])),
                ('place_type', models.CharField(choices=[('cn', 'Country'), ('fl', 'First-level subdivision'), ('cd', 'County or District'), ('tw', 'Town'), ('ct', 'City'), ('vl', 'Village'), ('fp', 'Fictional Place')], max_length=20)),
                ('travel_status', models.CharField(choices=[('b', 'Been there.'), ('m', 'Want to visit so much'), ('w', 'Want to visit'), ('l', 'I live here.'), ('u', 'Used to live here')], max_length=40)),
                ('rank', models.CharField(blank=True, choices=[('a', '1'), ('b', '2'), ('c', '3'), ('d', '4'), ('e', '5')], max_length=12, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='things.Director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='starring',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='things.Actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='watch_status',
            field=models.CharField(choices=[('w', 'Watched'), ('n', 'Not watched'), ('s', 'Started'), ('h', 'Halfway through')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='watch_status',
            field=models.CharField(choices=[('w', 'Watched'), ('n', 'Not watched'), ('s', 'Started'), ('h', 'Halfway through')], max_length=20, null=True),
        ),
    ]
