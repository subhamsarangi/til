from django.contrib import admin

from .models import *

admin.site.register(Profile)
admin.site.register(Settings)

class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'country', 'dob')
    list_filter = ['country']

admin.site.register(Actor, ActorAdmin)
admin.site.register(Director)
admin.site.register(Writer)
admin.site.register(Musician)
admin.site.register(Artist)
admin.site.register(Dancer)
admin.site.register(SportsPerson)

admin.site.register(FitnessPerson)
admin.site.register(FemaleModel)
admin.site.register(AdultModel)

admin.site.register(VideoGenre)
admin.site.register(AudioGenre)

admin.site.register(Movie)
admin.site.register(TVShow)
admin.site.register(Anime)
admin.site.register(Book)
admin.site.register(Song)

admin.site.register(YoutubeChannel)
admin.site.register(Application)
admin.site.register(Website)

admin.site.register(Place)
admin.site.register(Food)
admin.site.register(Vehicle)