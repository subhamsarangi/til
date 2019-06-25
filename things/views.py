from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *
from .forms import *

def register(request):
    success_url = '/login'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = UserCreationForm()
    args = {'form': form}
    return render(request, 'registration/register.html', args)

class HomeView(View):
    template_name='things/home.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            actor_list = Actor.objects.filter(
                ~Q(owner=self.request.user)&
                Q(is_private=False)
                ).order_by('?')[:5]
            vehicle_list = Vehicle.objects.filter(
                ~Q(owner=self.request.user)&
                Q(is_private=False)
                ).order_by('?')[:5]
            musician_list = Musician.objects.filter(
                ~Q(owner=self.request.user)&
                Q(is_private=False)
                ).order_by('?')[:5]
            movie_list = Movie.objects.filter(
                ~Q(owner=self.request.user)&
                Q(is_private=False)
                ).order_by('?')[:5]
            tv_list = TVShow.objects.filter(
                ~Q(owner=self.request.user)&
                Q(is_private=False)
                ).order_by('?')[:5]
            anime_list = Anime.objects.filter(
                ~Q(owner=self.request.user)&
                Q(is_private=False)
                ).order_by('?')[:5]
        else:
            actor_list = Actor.objects.filter(
                is_private=False
                ).distinct().order_by('?')[:5]
            vehicle_list = Vehicle.objects.filter(
                is_private=False
                ).order_by('?')[:5]
            musician_list = Musician.objects.filter(
                is_private=False
                ).order_by('?')[:5]
            movie_list = Movie.objects.filter(
                is_private=False
                ).order_by('?')[:5]
            tvshow_list = TVShow.objects.filter(
                is_private=False
                ).order_by('?')[:5]
            anime_list = Anime.objects.filter(
                is_private=False
                ).order_by('?')[:5]
        context = {
            'actor_list':actor_list,
            'vehicle_list':vehicle_list,
            'musician_list':musician_list,
            'movie_list':movie_list,
            'tvshow_list':tvshow_list,
            'anime_list':anime_list,
        }
        return render(request, self.template_name, context)


def user_profile(request, user_slug):
    uprofile = get_object_or_404(Profile, slug=user_slug)
    return render(request, 'things/user.html', {'uprofile': uprofile})

class ProfileView(DetailView, LoginRequiredMixin):
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Profile.objects.filter(owner=self.request.user)
        else:
            return Profile.objects.filter(owner=-1)

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class=ProfileUpdateForm
    template_name='things/form.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(ProfileUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().slug
        ctx['formtitle'] = 'Account: {}'.format(name)
        ctx['formbutton'] = 'Save Changes'
        return ctx

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise Http404
        return Profile.objects.filter(owner=self.request.user)

class SettingsUpdateView(LoginRequiredMixin, UpdateView):
    form_class=SettingsUpdateForm
    template_name='things/form.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(SettingsUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().slug
        ctx['formtitle'] = 'Settings: {}'.format(name)
        ctx['formbutton'] = 'Save Changes'
        return ctx

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise Http404
        return Settings.objects.filter(owner=self.request.user)

class ActorCreateView(LoginRequiredMixin, CreateView):
    form_class=ActorCreateForm
    template_name='things/form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(ActorCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(ActorCreateView, self).get_context_data(**kwargs)
        ctx['formtitle'] = 'Add new Actor'
        ctx['formbutton'] = 'Create'
        return ctx


class ActorUpdateView(LoginRequiredMixin, UpdateView):
    form_class=ActorUpdateForm
    template_name='things/form.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(ActorUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        ctx['formtitle'] = 'Updating: {}'.format(name)
        ctx['formbutton'] = 'Save Changes'
        return ctx

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise Http404
        return Actor.objects.filter(owner=self.request.user)

class ActorDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('things:actors')
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(ActorDeleteView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj

    def get_queryset(self):
        return Actor.objects.filter(owner=self.request.user)

class ActorDetailView(DetailView):
    def get_queryset(self):
        return Actor.objects.all()

class ActorListView(ListView):
    paginate_by = 15
    def get_queryset(self):
        try:
            slug = self.kwargs.get("slug")
            if slug:
                if slug=='latest':
                    queryset = Actor.objects.filter(is_private=False).order_by('-timestamp')
                elif slug=='oldest':
                    queryset = Actor.objects.filter(is_private=False).order_by('timestamp')
                else:
                    queryset = Actor.objects.filter(
                        Q(is_private=False) & 
                        (Q(name=slug) |
                        Q(name__icontains=slug))
                    ).order_by('name')
            else:
                queryset = Actor.objects.filter(is_private=False).order_by('name')
            return queryset
        except PageNotAnInteger:
            paginator = Paginator(queryset, self.paginate_by)
            page = self.request.GET.get('page')
            return paginator.page(1)
        except EmptyPage:
            paginator = Paginator(queryset, self.paginate_by)
            page = self.request.GET.get('page')
            return paginator.page(paginator.num_pages)


class VehicleCreateView(LoginRequiredMixin, CreateView):
    form_class=VehicleCreateForm
    template_name='things/form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(VehicleCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(VehicleCreateView, self).get_context_data(**kwargs)
        ctx['formtitle'] = 'Add new Vehicle'
        ctx['formbutton'] = 'Create'
        return ctx


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    form_class=VehicleUpdateForm
    template_name='things/form.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(VehicleUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        ctx['formtitle'] = 'Updating: {}'.format(name)
        ctx['formbutton'] = 'Save Changes'
        return ctx

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise Http404
        return Vehicle.objects.filter(owner=self.request.user)

class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('things:vehicles')
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(VehicleDeleteView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj

    def get_queryset(self):
        return Vehicle.objects.filter(owner=self.request.user)

class VehicleDetailView(DetailView):
    def get_queryset(self):
        return Vehicle.objects.all()

class VehicleListView(ListView):
    def get_queryset(self):
        try:
            slug = self.kwargs.get("slug")
            if slug:
                queryset = Vehicle.objects.filter(
                    Q(is_private=True) & 
                    (Q(name=slug) |
                    Q(name__icontains=slug))
                )
            else:
                queryset = Vehicle.objects.filter(is_private=False)
            return queryset
        except PageNotAnInteger:
            paginator = Paginator(queryset, self.paginate_by)
            page = self.request.GET.get('page')
            return paginator.page(1)
        except EmptyPage:
            paginator = Paginator(queryset, self.paginate_by)
            page = self.request.GET.get('page')
            return paginator.page(paginator.num_pages)


class MusicianCreateView(LoginRequiredMixin, CreateView):
    form_class=MusicianCreateForm
    template_name='things/form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(MusicianCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(MusicianCreateView, self).get_context_data(**kwargs)
        ctx['formtitle'] = 'Add new Musician'
        ctx['formbutton'] = 'Create'
        return ctx


class MusicianUpdateView(LoginRequiredMixin, UpdateView):
    form_class=MusicianUpdateForm
    template_name='things/form.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(MusicianUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        ctx['formtitle'] = 'Updating: {}'.format(name)
        ctx['formbutton'] = 'Save Changes'
        return ctx

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise Http404
        return Musician.objects.filter(owner=self.request.user)

class MusicianDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('things:Musicians')
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(MusicianDeleteView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj

    def get_queryset(self):
        return Musician.objects.filter(owner=self.request.user)

class MusicianDetailView(DetailView):
    def get_queryset(self):
        return Musician.objects.all()

class MusicianListView(ListView):
    paginate_by = 15
    def get_queryset(self):
        try:
            slug = self.kwargs.get("slug")
            if slug:
                queryset = Musician.objects.filter(
                    Q(is_private=False) & 
                    (Q(name=slug) |
                    Q(name__icontains=slug)).order_by('name')
                )
            else:
                queryset = Musician.objects.filter(is_private=False).order_by('name')
            return queryset
        except PageNotAnInteger:
            paginator = Paginator(queryset, self.paginate_by)
            page = self.request.GET.get('page')
            return paginator.page(1)
        except EmptyPage:
            paginator = Paginator(queryset, self.paginate_by)
            page = self.request.GET.get('page')
            return paginator.page(paginator.num_pages)


class MovieCreateView(LoginRequiredMixin, CreateView):
    form_class=MovieCreateForm
    template_name='things/form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(MovieCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(MovieCreateView, self).get_context_data(**kwargs)
        ctx['formtitle'] = 'Add new Movie'
        ctx['formbutton'] = 'Create'
        return ctx

    def get_form_kwargs(self):
        kwargs=super(MovieCreateView, self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs

class MovieUpdateView(LoginRequiredMixin, UpdateView):
    form_class=MovieUpdateForm
    template_name='things/form.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(MovieUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        ctx['formtitle'] = 'Updating: {}'.format(name)
        ctx['formbutton'] = 'Save Changes'
        return ctx

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise Http404
        return Movie.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs=super(MovieUpdateView, self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs

class MovieDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('things:Movies')
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(MovieDeleteView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj

    def get_queryset(self):
        return Movie.objects.filter(owner=self.request.user)

class MovieDetailView(DetailView):
    def get_queryset(self):
        return Movie.objects.all()

class MovieListView(ListView):
    paginate_by = 15
    def get_queryset(self):
        try:
            slug = self.kwargs.get("slug")
            if slug:
                queryset = Movie.objects.filter(
                    Q(is_private=False) & 
                    (Q(name=slug) |
                    Q(name__icontains=slug)).order_by('name')
                )
            else:
                queryset = Movie.objects.filter(is_private=False).order_by('name')
            return queryset
        except PageNotAnInteger:
            paginator = Paginator(queryset, self.paginate_by)
            page = self.request.GET.get('page')
            return paginator.page(1)
        except EmptyPage:
            paginator = Paginator(queryset, self.paginate_by)
            page = self.request.GET.get('page')
            return paginator.page(paginator.num_pages)


class TVShowCreateView(LoginRequiredMixin, CreateView):
    form_class=TVShowCreateForm
    template_name='things/form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(TVShowCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(TVShowCreateView, self).get_context_data(**kwargs)
        ctx['formtitle'] = 'Add new TVShow'
        ctx['formbutton'] = 'Create'
        return ctx

    def get_form_kwargs(self):
        kwargs=super(TVShowCreateView, self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs


class TVShowUpdateView(LoginRequiredMixin, UpdateView):
    form_class=TVShowUpdateForm
    template_name='things/form.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(TVShowUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        ctx['formtitle'] = 'Updating: {}'.format(name)
        ctx['formbutton'] = 'Save Changes'
        return ctx

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise Http404
        return TVShow.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs=super(TVShowUpdateView, self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs

class TVShowDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('things:TVShows')
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(TVShowDeleteView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj

    def get_queryset(self):
        return TVShow.objects.filter(owner=self.request.user)

class TVShowDetailView(DetailView):
    def get_queryset(self):
        return TVShow.objects.all()

class TVShowListView(ListView):
    paginate_by = 15
    def get_queryset(self):
        try:
            slug = self.kwargs.get("slug")
            if slug:
                queryset = TVShow.objects.filter(
                    Q(is_private=False) & 
                    (Q(name=slug) |
                    Q(name__icontains=slug)).order_by('name')
                )
            else:
                queryset = TVShow.objects.filter(is_private=False).order_by('name')
            return queryset
        except PageNotAnInteger:
            paginator = Paginator(queryset, self.paginate_by)
            page = self.request.GET.get('page')
            return paginator.page(1)
        except EmptyPage:
            paginator = Paginator(queryset, self.paginate_by)
            page = self.request.GET.get('page')
            return paginator.page(paginator.num_pages)


class AnimeCreateView(LoginRequiredMixin, CreateView):
    form_class=AnimeCreateForm
    template_name='things/form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(AnimeCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(AnimeCreateView, self).get_context_data(**kwargs)
        ctx['formtitle'] = 'Add new Anime'
        ctx['formbutton'] = 'Create'
        return ctx


class AnimeUpdateView(LoginRequiredMixin, UpdateView):
    form_class=AnimeUpdateForm
    template_name='things/form.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(AnimeUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        ctx['formtitle'] = 'Updating: {}'.format(name)
        ctx['formbutton'] = 'Save Changes'
        return ctx

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise Http404
        return Anime.objects.filter(owner=self.request.user)

class AnimeDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('things:Animes')
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(AnimeDeleteView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj

    def get_queryset(self):
        return Anime.objects.filter(owner=self.request.user)

class AnimeDetailView(DetailView):
    def get_queryset(self):
        return Anime.objects.all()

class AnimeListView(ListView):
    paginate_by = 15
    def get_queryset(self):
        try:
            slug = self.kwargs.get("slug")
            if slug:
                queryset = Anime.objects.filter(
                    Q(is_private=False) & 
                    (Q(name=slug) |
                    Q(name__icontains=slug)).order_by('name')
                )
            else:
                queryset = Anime.objects.filter(is_private=False).order_by('name')
            return queryset
        except PageNotAnInteger:
            paginator = Paginator(queryset, self.paginate_by)
            page = self.request.GET.get('page')
            return paginator.page(1)
        except EmptyPage:
            paginator = Paginator(queryset, self.paginate_by)
            page = self.request.GET.get('page')
            return paginator.page(paginator.num_pages)
