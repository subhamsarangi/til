import os

from django.db import models
from django.db.models import F
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from django.contrib.auth.models import User as UserModel
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django_countries.fields import CountryField

from .utils import *

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    owner           =models.ForeignKey(User)
    first_name      =models.CharField(max_length=50, blank=True, null=True,validators=[alphanumspacedash])
    last_name       =models.CharField(max_length=50, blank=True, null=True, validators=[alphanumspacedash])
    dob             =models.DateField(blank=True, null=True)
    location        =models.CharField(null=True, blank=True, max_length = 50)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.owner.username
    
    def get_absolute_url(self):
        return reverse('things:profile', kwargs={'slug':self.slug})

    def get_initials(self):
        initial =''
        if not (self.first_name and self.last_name):
            initial=self.owner.username[0]
        else:
            if self.first_name:
                initial+=self.first_name[0]
            if self.last_name:
                initial+=self.last_name[0]
        return initial

    class Meta:
        ordering = ('owner','timestamp',)

    @property
    def title(self):
        return self.owner.username

class Settings(models.Model):
    owner = models.ForeignKey(User)
    show_actors =models.BooleanField(default=False)
    show_directors =models.BooleanField(default=False)
    show_writers =models.BooleanField(default=False)
    show_artists =models.BooleanField(default=False)
    show_musicians =models.BooleanField(default=False)
    show_dancers =models.BooleanField(default=False)
    show_sportspersons =models.BooleanField(default=False)
    show_fitnesspersons =models.BooleanField(default=False)
    show_femalemodels =models.BooleanField(default=False)
    show_songs =models.BooleanField(default=False)
    show_movies =models.BooleanField(default=False)
    show_tvshows =models.BooleanField(default=False)
    show_animes =models.BooleanField(default=False)
    show_books =models.BooleanField(default=False)
    show_foods =models.BooleanField(default=False)
    show_youtubechannels =models.BooleanField(default=False)
    show_websites =models.BooleanField(default=False)
    show_apps =models.BooleanField(default=False)
    show_videogames =models.BooleanField(default=False)
    show_cars=models.BooleanField(default=False)
    show_bikes =models.BooleanField(default=False)
    show_adultmodels =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.owner.username
    
    def get_absolute_url(self):
        return reverse('things:profile', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('owner','timestamp',)
        verbose_name_plural = "settings"

    @property
    def title(self):
        return self.owner.username


def user_registration_receiver(sender, instance, *args, **kwargs):
    if not Profile.objects.filter(owner=instance):
        newpro=Profile.objects.create(owner=instance)
        newpro.slug=instance.username
        newpro.save()
    if not Settings.objects.filter(owner=instance):
        newset=Settings.objects.create(owner=instance)
        newset.slug=instance.username
        newset.save()

post_save.connect(user_registration_receiver, sender=UserModel)

class Actor(models.Model):
    genders = (
		('f', 'Female'),
        ('m', 'Male'),
        ('o', 'Not Specified'),
    )
    def update_image_file(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (instance.slug, ext)
        return os.path.join('actors', filename)

    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphanumspacedash])
    gender          =models.CharField(choices=genders, blank=False, max_length=12, default='o')
    country         =CountryField(blank_label='(select country)')
    dob             =models.DateField(blank=False, default='01/01/89')
    image           =models.ImageField(upload_to=update_image_file, blank=True, null=True)
    insta           =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:actor', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name')
        unique_together = ('owner', 'rank', 'gender')

    @property
    def is_female(self):
        if self.gender == 'f':
            return True
        else:
            return False

    @property
    def title(self):
        return self.name


class Director(models.Model):    
    def update_image_file(instance, filename):
        pass

    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphanumspacedash])
    country         =CountryField(blank_label='(select country)')
    is_active	    =models.BooleanField(default=True)
    image_url        =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:director', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank')

    @property
    def title(self):
        return self.name


class Writer(models.Model):
    genders = (
		('f', 'Female'),
        ('m', 'Male'),
    )
    def update_image_file(instance, filename):
        pass

    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphanumspacedashq])
    gender          =models.CharField(choices=genders, blank=False, max_length=20)
    genres          =models.CharField(blank=False, max_length=80)
    languages       =models.CharField(blank=False, max_length=80)
    country         =CountryField(blank_label='(select country)')
    is_active	    =models.BooleanField(default=True)
    image_url        =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:writer', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank')

    @property
    def title(self):
        return self.name


class Artist(models.Model):
    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphanumspacedashq])
    country         =CountryField(blank_label='(select country)')
    genres          =models.CharField(blank=False, max_length=80)
    is_active	    =models.BooleanField(default=True)
    image_url       =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('things:artist', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank')

    @property
    def title(self):
        return self.name


class Musician(models.Model):
    mtypes = (
		('fs', 'Female Singer'),
        ('ms', 'Male Singer'),
        ('bs', 'Band/Duo/Group'),
    )
    def update_image_file(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (instance.slug, ext)
        return os.path.join('musicians', filename)

    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphanumspacedashq])
    mtype           =models.CharField(choices=mtypes, blank=False, max_length=20)
    country         =CountryField(blank_label='(select country)')
    languages       =models.CharField(blank=False, max_length=80)
    genres          =models.CharField(blank=False, max_length=80)
    is_active	    =models.BooleanField(default=True)
    image           =models.ImageField(upload_to=update_image_file, blank=True, null=True)
    insta           =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:musician', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank', 'mtype')

    @property
    def title(self):
        return self.name


class Dancer(models.Model):
    def update_image_file(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (instance.slug, ext)
        return os.path.join('dancers', filename)

    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphanumspacedashq])
    country         =CountryField(blank_label='(select country)')
    image           =models.ImageField(upload_to=update_image_file, blank=True, null=True)
    insta           =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:dancer', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank')

    @property
    def title(self):
        return self.name


class SportsPerson(models.Model):
    genders = (
		('f', 'Female'),
        ('m', 'Male'),
    )

    def update_image_file(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (instance.slug, ext)
        return os.path.join('sportspersons', filename)

    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphanumspacedashq])
    gender          =models.CharField(choices=genders, blank=False, max_length=20)
    country         =CountryField(blank_label='(select country)')
    image           =models.ImageField(upload_to=update_image_file, blank=True, null=True)
    insta           =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:sportsperson', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank')
        verbose_name_plural = "Sports Persons"

    @property
    def title(self):
        return self.name


class FitnessPerson(models.Model):    
    genders = (
		('f', 'Female'),
        ('m', 'Male'),
    )

    def update_image_file(instance, filename):
        pass

    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphanumspacedashq])
    gender          =models.CharField(choices=genders, blank=False, max_length=20)
    image_url       =models.URLField(max_length=300, blank=True, null=True)
    insta           =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:fitnessperson', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank')
        verbose_name_plural = "Fitness Persons"

    @property
    def title(self):
        return self.name


class FemaleModel(models.Model):
    def update_image_file(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (instance.slug, ext)
        return os.path.join('models', filename)

    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphanumspacedashq])
    country         =CountryField(blank_label='(select country)')
    image           =models.ImageField(upload_to=update_image_file, blank=True, null=True)
    insta           =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:model', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank')
        verbose_name_plural = "Female Models"

    @property
    def title(self):
        return self.name


class AdultModel(models.Model):
    def update_image_file(instance, filename):
        pass

    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphanumspacedashq])
    real_name       =models.CharField(max_length=50, blank=True, null=True, validators=[alphanumspacedashq])
    image_url        =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:adult', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank')
        verbose_name_plural = "Adult Models"

    @property
    def title(self):
        return self.name

class VideoGenre(models.Model):
    name            =models.CharField(max_length=80, blank=False, validators=[alphasymspace])
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Video Genres"

class AudioGenre(models.Model):
    name            =models.CharField(max_length=80, blank=False, validators=[alphasymspace])
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Audio Genres"

class Movie(models.Model):
    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphasymspace])
    genre           =models.ManyToManyField(VideoGenre, blank=False)
    watch_status    =models.CharField(choices=mv_watch_statuses, max_length=20, blank=False, null=True)
    poster          =models.URLField(max_length=200, blank=True, null=True)
    starring        =models.ManyToManyField(Actor, blank=True)
    director        =models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True)
    year            =models.IntegerField(blank=False,null=True, validators=[positivenum])
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:movie', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank')

    @property
    def title(self):
        return self.name


class TVShow(models.Model):
    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphasymspace])
    genre           =models.ManyToManyField(VideoGenre, blank=False)
    watch_status    =models.CharField(choices=tv_watch_statuses, max_length=20, blank=False, null=True)
    starring        =models.ManyToManyField(Actor, blank=True)
    poster          =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:tvshow', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank')
        verbose_name_plural = "TV Shows"

    @property
    def title(self):
        return self.name


class Anime(models.Model):
    anime_types = (
        ('s', 'Series'),
        ('m', 'Movie'),
    )
    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphasymspace])
    anime_type      =models.CharField(choices=anime_types, blank=True, default='s',max_length=20)
    watch_status    =models.CharField(choices=tv_watch_statuses, max_length=20, blank=False)
    poster          =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:anime', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank', 'anime_type')
        verbose_name_plural = "Anime Series"

    @property
    def title(self):
        return self.name


class Book(models.Model):
    read_statuses = (
        ('rd', 'Read'),
        ('nr', 'Not read'),
        ('st', 'Started'),
        ('ht', 'Halfway through'),
        ('ad', 'Almost Done'),
    )
    sources = (
        ('ph', 'I own a physical copy'),
        ('eb', 'I have an eBook'),
        ('lb', 'Got it at the Library'),
        ('br', 'Borrowed from someone'),
        ('wb', 'Reading it on a website'),
    )
    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphasymspace])
    writers         =models.CharField(max_length=100, blank=False, null=True, validators=[alphasymspace])
    read_status     =models.CharField(choices=read_statuses, max_length=20, blank=False)
    source          =models.CharField(choices=sources, blank=False, max_length=40)
    cover           =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:book', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank')

    @property
    def title(self):
        return self.name


class Song(models.Model):
    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=80, blank=False, validators=[alphasymspace])
    singer          =models.CharField(max_length=80, blank=False, validators=[alphasymspace])
    cover_url       =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:song', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank')

    @property
    def title(self):
        return self.name


class YoutubeChannel(models.Model):
    channel_types = (
        ('tu', 'Tutorial'),
        ('ts', 'Talk Show Host'),
        ('ed', 'Educational'),
        ('en', 'Entertainment'),
        ('fo', 'Food'),
        ('so', 'Social'),
        ('te', 'Tech'),
        ('mx', 'Mixed'),
    )
    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphasymspace])
    channel_type    =models.CharField(choices=channel_types, max_length=20, blank=False)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:youtubechannel', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank')
        verbose_name_plural = "Youtube Channels"

    @property
    def title(self):
        return self.name


class Application(models.Model):
    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=40, blank=False, validators=[alphasymspace])
    app_type        =models.CharField(choices=site_types, max_length=20, blank=False)
    inactive        =models.BooleanField(default=False)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:application', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank')

    @property
    def title(self):
        return self.name


class Website(models.Model):
    owner           =models.ForeignKey(User)
    link_url        =models.URLField(max_length=300, blank=True, null=True)
    name            =models.CharField(max_length=40, blank=False, validators=[alphasymspace])
    site_type       =models.CharField(choices=site_types, max_length=20, blank=False)
    inactive        =models.BooleanField(default=False)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:website', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank')

    @property
    def title(self):
        return self.name



class Place(models.Model):
    place_types = (
        ('cn', 'Country'),
        ('fl', 'First-level subdivision'),
        ('cd', 'County or District'),
        ('tw', 'Town'),
        ('ct', 'City'),
        ('vl', 'Village'),
        ('fp', 'Fictional Place'),
    )
    travel_statuses = (
        ('b', 'Been there.'),
        ('m', 'Want to visit so much'),
        ('w', 'Want to visit'),
        ('l', 'I live here.'),
        ('u', 'Used to live here'),
    )
    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphasymspace])
    place_type      =models.CharField(choices=place_types, max_length=20, blank=False)
    travel_status   =models.CharField(choices=travel_statuses, blank=False, max_length=40)
    image_url       =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:place', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank','place_type')

    @property
    def title(self):
        return self.name


class Food(models.Model):
    cuisines = (
        ('cn', 'Bengali'),
        ('cn', 'North Indian'),
        ('cn', 'South Indian'),
        ('fl', 'Japanese'),
        ('vl', 'French'),
        ('cd', 'Italian'),
        ('vl', 'Arabic'),
        ('vl', 'Mexian'),
        ('tw', 'Thai'),
        ('ct', 'Vietnamese'),
        ('vl', 'American'),
        ('vl', 'German'),
        ('vl', 'Persian'),
        ('vl', 'Chinese'),
        ('vl', 'British'),
        ('vl', 'Ethipian'),
        ('fp', 'Fictional Place'),
    )
    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphasymspace])
    cuisine        =models.CharField(choices=cuisines, max_length=20, blank=False)
    want_to_eat     =models.BooleanField(default=False)
    can_cook        =models.BooleanField(default=False)
    image_url       =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:food', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank', 'cuisine')

    @property
    def title(self):
        return self.name


class Vehicle(models.Model):
    vehicle_types = (
        ('ca', 'Car'),
        ('bi', 'Bike'),
        ('ai', 'Aircraft'),
        ('wa', 'Watercraft'),
        ('ot', 'Others'),
    )
    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphasymspace])
    vehicle_type    =models.CharField(choices=vehicle_types, max_length=20, blank=False)
    company         =models.CharField(max_length=50, blank=True)
    image_url       =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_private      =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:vehicle', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('rank', 'name',)
        unique_together = ('owner', 'rank','vehicle_type')

    @property
    def title(self):
        return self.name

# videogame
# others

def act_pre_save_receiver(sender, instance, *args, **kwargs):
    image_modification_tool(instance.image, 400)
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def dir_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def wr_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def mu_pre_save_receiver(sender, instance, *args, **kwargs):
    image_modification_tool(instance.image, 400)
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def ar_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def da_pre_save_receiver(sender, instance, *args, **kwargs):
    image_modification_tool(instance.image, 400)
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def sp_pre_save_receiver(sender, instance, *args, **kwargs):
    image_modification_tool(instance.image, 400)
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def ft_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def mod_pre_save_receiver(sender, instance, *args, **kwargs):
    image_modification_tool(instance.image, 400)
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def adm_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name+'xxx')

def mv_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def tv_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def an_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def bk_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def sg_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def yc_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def ap_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def wb_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def pl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def fd_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def vh_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

pre_save.connect(act_pre_save_receiver, sender=Actor)
pre_save.connect(dir_pre_save_receiver, sender=Director)
pre_save.connect(wr_pre_save_receiver, sender=Writer)
pre_save.connect(mu_pre_save_receiver, sender=Musician)
pre_save.connect(ar_pre_save_receiver, sender=Artist)
pre_save.connect(da_pre_save_receiver, sender=Dancer)
pre_save.connect(sp_pre_save_receiver, sender=SportsPerson)
pre_save.connect(ft_pre_save_receiver, sender=FitnessPerson)
pre_save.connect(mod_pre_save_receiver, sender=FemaleModel)
pre_save.connect(adm_pre_save_receiver, sender=AdultModel)
pre_save.connect(mv_pre_save_receiver, sender=Movie)
pre_save.connect(tv_pre_save_receiver, sender=TVShow)
pre_save.connect(an_pre_save_receiver, sender=Anime)
pre_save.connect(bk_pre_save_receiver, sender=Book)
pre_save.connect(sg_pre_save_receiver, sender=Song)
pre_save.connect(yc_pre_save_receiver, sender=YoutubeChannel)
pre_save.connect(ap_pre_save_receiver, sender=Application)
pre_save.connect(wb_pre_save_receiver, sender=Website)
pre_save.connect(pl_pre_save_receiver, sender=Place)
pre_save.connect(fd_pre_save_receiver, sender=Food)
pre_save.connect(vh_pre_save_receiver, sender=Vehicle)
