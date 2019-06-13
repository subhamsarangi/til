import os

from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from django_countries.fields import CountryField

User = settings.AUTH_USER_MODEL

class Actor(models.Model):
    alphanumspacedash = RegexValidator(
        r'^[a-zA-Z0-9 -]*$', 'Alphanumeric characters, dash & space allowed.')

    genders = (
		('f', 'Female'),
        ('m', 'Male'),
        ('o', 'Not Specified'),
    )
    top_five = (
		('a', '1'),
        ('b', '2'),
        ('c', '3'),
        ('d', '4'),
        ('e', '5'),
    )
    def update_image_file(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (instance.slug, ext)
        return os.path.join('actors', filename)

    owner           =models.ForeignKey(User)
    name            =models.CharField(max_length=50, blank=False, validators=[alphanumspacedash])
    dob             =models.DateField(blank=False, default='01/01/89')
    gender          =models.CharField(choices=genders, blank=False, max_length=12, default='o')
    country         =CountryField(blank_label='(select country)')
    image           =models.ImageField(upload_to=update_image_file, blank=True, null=True)
    gender          =models.CharField(choices=top_five, blank=True, null=True, max_length=12)
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

def act_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = slugify(instance.name)

pre_save.connect(act_pre_save_receiver, sender=Actor)