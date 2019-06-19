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
        else:
            actor_list = Actor.objects.filter(
                is_private=False
                ).order_by('?')[:5]
            vehicle_list = Vehicle.objects.filter(
                is_private=False
                ).order_by('?')[:5]
        context = {
            'actor_list':actor_list,
            'vehicle_list':vehicle_list,

        }
        return render(request, self.template_name, context)


def user_profile(request, user_slug):
    uprofile = get_object_or_404(Profile, slug=user_slug)
    return render(request, 'things/user.html', {'uprofile': uprofile})

class ProfileView(DetailView, LoginRequiredMixin):
    def get_queryset(self):
        return Profile.objects.filter(owner=self.request.user)

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
                queryset = Actor.objects.filter(
                    Q(is_private=False) & 
                    (Q(name=slug) |
                    Q(name__icontains=slug))
                )
            else:
                queryset = Actor.objects.filter(is_private=False)
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
