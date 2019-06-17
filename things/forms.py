from django import forms
from .models import *

#CREATE FORMS
class ActorCreateForm(forms.ModelForm):
    class Meta:
        model = Actor
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

        labels = {
            'dob': ('Date of Birth'),
        }
        widgets = {
            'dob': forms.DateInput(attrs={'class':'datepicker'}),
        }


class DirectorCreateForm(forms.ModelForm):
    class Meta:
        model = Director
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class WriterCreateForm(forms.ModelForm):
    class Meta:
        model = Writer
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class ArtistCreateForm(forms.ModelForm):
    class Meta:
        model = Artist
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class MusicianCreateForm(forms.ModelForm):
    class Meta:
        model = Musician
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class DancerCreateForm(forms.ModelForm):
    class Meta:
        model = Dancer
        exclude = ['owner', 'slug', 'timestamp', 'updated',]


class SportsPersonCreateForm(forms.ModelForm):
    class Meta:
        model = SportsPerson
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class FitnessPersonCreateForm(forms.ModelForm):
    class Meta:
        model = FitnessPerson
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class FemaleModelCreateForm(forms.ModelForm):
    class Meta:
        model = FemaleModel
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class AdultModelCreateForm(forms.ModelForm):
    class Meta:
        model = AdultModel
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class MovieModelCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class TVShowModelCreateForm(forms.ModelForm):
    class Meta:
        model = TVShow
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class AnimeModelCreateForm(forms.ModelForm):
    class Meta:
        model = Anime
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class BookModelCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class SongModelCreateForm(forms.ModelForm):
    class Meta:
        model = Song
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class YoutubeChannelModelCreateForm(forms.ModelForm):
    class Meta:
        model = YoutubeChannel
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class ApplicationModelCreateForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class WebsiteModelCreateForm(forms.ModelForm):
    class Meta:
        model = Website
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class PlaceModelCreateForm(forms.ModelForm):
    class Meta:
        model = Place
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class FoodModelCreateForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class VehicleModelCreateForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class ActorUpdateForm(forms.ModelForm):
    class Meta:
        model = Actor
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

        labels = {
            'dob': ('Date of Birth'),
        }
        widgets = {
            'dob': forms.DateInput(attrs={'class':'datepicker'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['owner', 'slug', 'timestamp', 'updated',]
        widgets = {
            'dob': forms.DateInput(attrs={'class':'datepicker'}),
        }

class SettingsUpdateForm(forms.ModelForm):
    class Meta:
        model = Settings
        exclude = ['owner', 'slug', 'timestamp', 'updated',]
