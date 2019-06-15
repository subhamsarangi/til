from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^join/$', views.register, name='join'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),

    url(r'^actors/$', views.ActorListView.as_view(), name='actors'),
    url(r'^add-actor/$', views.ActorCreateView.as_view(),name='new_actor'),
    url(r'^actor/(?P<pk>\d+)/(?P<slug>[\w-]+)/edit$', views.ActorUpdateView.as_view(), name='edit_actor'),
    url(r'^actor/(?P<pk>\d+)/(?P<slug>[\w-]+)/delete/$', views.ActorDeleteView.as_view(),name='del_actor'),
    url(r'^actor/(?P<slug>[\w-]+)/$', views.ActorDetailView.as_view(), name='actor'),
    
]