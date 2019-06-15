import os
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django_countries.fields import CountryField

from .utils import *

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    owner = models.ForeignKey(User)
    first_name=models.CharField(max_length=50, blank=False, validators=[alphanumspacedash])
    last_name=models.CharField(max_length=50, blank=True, validators=[alphanumspacedash])
    dob =models.DateField(blank=True, default='01/01/89')
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)


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
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)


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
    image           =models.ImageField(upload_to=update_image_file, blank=True, null=True)
    dob             =models.DateField(blank=False, default='01/01/89')
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    insta           =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:actor', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

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
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    remarks         =models.TextField(blank=True, null=True)
    image_url        =models.URLField(max_length=200, blank=True, null=True)
    is_active	    =models.BooleanField(default=False)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:director', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

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
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    image_url        =models.URLField(max_length=200, blank=True, null=True)
    is_active	    =models.BooleanField(default=False)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:writer', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

    @property
    def title(self):
        return self.name


class Artist(models.Model):
    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphanumspacedashq])
    country         =CountryField(blank_label='(select country)')
    genres          =models.CharField(blank=False, max_length=80)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_active	    =models.BooleanField(default=False)
    image_url       =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('things:artist', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

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
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    is_active	    =models.BooleanField(default=False)
    image           =models.ImageField(upload_to=update_image_file, blank=True, null=True)
    insta           =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:musician', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

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
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    image           =models.ImageField(upload_to=update_image_file, blank=True, null=True)
    insta           =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:dancer', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

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
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    image           =models.ImageField(upload_to=update_image_file, blank=True, null=True)
    insta           =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:sportsperson', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

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
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    image_url       =models.URLField(max_length=300, blank=True, null=True)
    insta           =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:fitnessperson', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

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
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    image           =models.ImageField(upload_to=update_image_file, blank=True, null=True)
    insta           =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:model', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

    @property
    def title(self):
        return self.name


class AdultModel(models.Model):
    def update_image_file(instance, filename):
        pass

    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphanumspacedashq])
    real_name       =models.CharField(max_length=50, blank=True, null=True, validators=[alphanumspacedashq])
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    image_url        =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:adult', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

    @property
    def title(self):
        return self.name


class Movie(models.Model):
    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphasymspace])
    watch_status    =models.CharField(choices=watch_statuses, max_length=20, blank=False, null=True)
    genre           =models.CharField(choices=movie_tv_genre, blank=False, max_length=20)
    year            =models.IntegerField(blank=False,null=True, validators=[positivenum])
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    poster          =models.URLField(max_length=200, blank=True, null=True)
    director        =models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True)
    starring        =models.ManyToManyField(Actor, blank=True)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:movie', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

    @property
    def title(self):
        return self.name


class TVShow(models.Model):
    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphasymspace])
    watch_status    =models.CharField(choices=watch_statuses, max_length=20, blank=False, null=True)
    genre           =models.CharField(choices=movie_tv_genre, blank=False, max_length=20)
    starring        =models.ManyToManyField(Actor, blank=True)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    poster          =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:tvshow', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

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
    watch_status    =models.CharField(choices=watch_statuses, max_length=20, blank=False)
    anime_type      =models.CharField(choices=anime_types, blank=False, max_length=20)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    poster          =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:anime', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

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
    read_status     =models.CharField(choices=read_statuses, max_length=20, blank=False)
    source          =models.CharField(choices=sources, blank=False, max_length=40)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    cover           =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:book', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

    @property
    def title(self):
        return self.name


class Song(models.Model):
    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=80, blank=False, validators=[alphasymspace])
    singer          =models.ForeignKey(Musician, on_delete=models.CASCADE, blank=False)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    cover_url       =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:song', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

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
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:youtubechannel', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

    @property
    def title(self):
        return self.name


class Application(models.Model):
    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=40, blank=False, validators=[alphasymspace])
    app_type        =models.CharField(choices=site_types, max_length=20, blank=False)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    inactive        =models.BooleanField(default=False)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:application', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

    @property
    def title(self):
        return self.name


class Website(models.Model):
    owner           =models.ForeignKey(User)
    link_url        =models.URLField(max_length=300, blank=True, null=True)
    name            =models.CharField(max_length=40, blank=False, validators=[alphasymspace])
    site_type       =models.CharField(choices=site_types, max_length=20, blank=False)
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    inactive        =models.BooleanField(default=False)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:website', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

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
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    image_url       =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:place', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

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
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    image_url       =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:food', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

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
    rank            =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
    image_url       =models.URLField(max_length=200, blank=True, null=True)
    remarks         =models.TextField(blank=True, null=True)
    slug            =models.SlugField(blank=True, null=True)
    timestamp       =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('things:place', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('name',)

    @property
    def title(self):
        return self.name

# videogame
# others

def act_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        image_modification_tool(instance.image, 500)
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
    if not instance.slug:
        image_modification_tool(instance.image, 500)
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def ar_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def da_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        image_modification_tool(instance.image, 500)
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def sp_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        image_modification_tool(instance.image, 500)
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def ft_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = unique_slug_generator(instance.name)

def mod_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        image_modification_tool(instance.image, 500)
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
