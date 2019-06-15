from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy

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
            actor_list = Actor.objects.filter(~Q(owner=self.request.user))
        else:
            actor_list = Actor.objects.all().order_by('?')
        context = {
            'actor_list':actor_list,
        }
        return render(request, self.template_name, context)

class ProfileView(View):
    template_name='things/profile.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            actor_list = Actor.objects.filter(owner=self.request.user)
            context = {
                'actor_list':actor_list,
            }
        else:
            context= {}

        return render(request, self.template_name, context)


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
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = Actor.objects.filter(
                Q(name=slug) |
                Q(name__icontains=slug)
            )
        else:
            queryset = Actor.objects.all()
        return queryset