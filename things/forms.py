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

class MusicianCreateForm(forms.ModelForm):
    class Meta:
        model = Musician
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class WriterCreateForm(forms.ModelForm):
    class Meta:
        model = Writer
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class FemaleModelCreateForm(forms.ModelForm):
    class Meta:
        model = FemaleModel
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class AdultModelCreateForm(forms.ModelForm):
    class Meta:
        model = AdultModel
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

class DirectorUpdateForm(forms.ModelForm):
    class Meta:
        model = Director
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class MusicianUpdateForm(forms.ModelForm):
    class Meta:
        model = Musician
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

# UPDATE FORMS
class WriterUpdateForm(forms.ModelForm):
    class Meta:
        model = Writer
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class FemaleModelUpdateForm(forms.ModelForm):
    class Meta:
        model = FemaleModel
        exclude = ['owner', 'slug', 'timestamp', 'updated',]

class AdultModelUpdateForm(forms.ModelForm):
    class Meta:
        model = AdultModel
        exclude = ['owner', 'slug', 'timestamp', 'updated',]