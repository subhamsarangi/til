from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url(r'^join/$', views.register, name='join'),
    url(r'^profile/(?P<slug>[\w-]+)/$', views.ProfileView.as_view(), name='profile'),
    url(r'^profile/(?P<pk>\d+)/(?P<slug>[\w-]+)/edit$', views.ProfileUpdateView.as_view(), name='edit_profile'),
    url(r'^settings/(?P<pk>\d+)/(?P<slug>[\w-]+)/edit$', views.SettingsUpdateView.as_view(), name='edit_settings'),

    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^user/(?P<user_slug>[\w-]+)/$', views.user_profile, name='user'),

    url(r'^actors/$', views.ActorListView.as_view(), name='actors'),
    url(r'^add-actor/$', views.ActorCreateView.as_view(),name='new_actor'),
    url(r'^actor/(?P<pk>\d+)/(?P<slug>[\w-]+)/edit$', views.ActorUpdateView.as_view(), name='edit_actor'),
    url(r'^actor/(?P<pk>\d+)/(?P<slug>[\w-]+)/delete/$', views.ActorDeleteView.as_view(),name='del_actor'),
    url(r'^actor/(?P<slug>[\w-]+)/$', views.ActorDetailView.as_view(), name='actor'),

    url(r'^vehicles/$', views.VehicleListView.as_view(), name='vehicles'),
    url(r'^add-vehicle/$', views.VehicleCreateView.as_view(),name='new_vehicle'),
    url(r'^vehicle/(?P<pk>\d+)/(?P<slug>[\w-]+)/edit$', views.VehicleUpdateView.as_view(), name='edit_vehicle'),
    url(r'^vehicle/(?P<pk>\d+)/(?P<slug>[\w-]+)/delete/$', views.VehicleDeleteView.as_view(),name='del_vehicle'),
    url(r'^vehicle/(?P<slug>[\w-]+)/$', views.VehicleDetailView.as_view(), name='vehicle'),
]