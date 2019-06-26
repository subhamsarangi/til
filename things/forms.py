from django import forms
from .models import *

#CREATE FORMS
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


class VehicleCreateForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class VehicleUpdateForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ['owner', 'slug', 'timestamp', 'updated',]


class MusicianCreateForm(forms.ModelForm):
    class Meta:
        model = Musician
        exclude = ['owner', 'slug', 'timestamp', 'updated',]
        labels = {
            'mtype': ('Type'),
        }

class MusicianUpdateForm(forms.ModelForm):
    class Meta:
        model = Musician
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

    def __init__(self, user=None, *args, **kwargs):
        super(MovieCreateForm, self).__init__(*args, **kwargs)
        self.fields['starring'].queryset = Actor.objects.filter(owner=user)

class MovieUpdateForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

    def __init__(self, user=None, *args, **kwargs):
        super(MovieUpdateForm, self).__init__(*args, **kwargs)
        self.fields['starring'].queryset = Actor.objects.filter(owner=user)

class TVShowCreateForm(forms.ModelForm):
    class Meta:
        model = TVShow
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

    def __init__(self, user=None, *args, **kwargs):
        super(TVShowCreateForm, self).__init__(*args, **kwargs)
        self.fields['starring'].queryset = Actor.objects.filter(owner=user)

class TVShowUpdateForm(forms.ModelForm):
    class Meta:
        model = TVShow
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

    def __init__(self, user=None, *args, **kwargs):
        super(TVShowUpdateForm, self).__init__(*args, **kwargs)
        self.fields['starring'].queryset = Actor.objects.filter(owner=user)


class AnimeCreateForm(forms.ModelForm):
    class Meta:
        model = Anime
        exclude = ['owner', 'slug', 'timestamp', 'updated','anime_type',]

class AnimeUpdateForm(forms.ModelForm):
    class Meta:
        model = Anime
        exclude = ['owner', 'slug', 'timestamp', 'updated','anime_type',]


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

class FemaleCreateForm(forms.ModelForm):
    class Meta:
        model = FemaleModel
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class AdultCreateForm(forms.ModelForm):
    class Meta:
        model = AdultModel
        exclude = ['owner', 'slug', 'timestamp', 'updated',]


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class SongCreateForm(forms.ModelForm):
    class Meta:
        model = Song
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class YoutubeChannelCreateForm(forms.ModelForm):
    class Meta:
        model = YoutubeChannel
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class ApplicationCreateForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class WebsiteCreateForm(forms.ModelForm):
    class Meta:
        model = Website
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class PlaceCreateForm(forms.ModelForm):
    class Meta:
        model = Place
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class FoodCreateForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = ['owner', 'slug', 'timestamp', 'updated',]
