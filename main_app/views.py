from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.shortcuts import redirect
from django.views import View


from .models import Finch, Song


class Home(TemplateView):
    template_name = 'home.html'


class FinchList(TemplateView):
    template_name = "finch_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["finches"] = Finch.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["finches"] = Finch.objects.all()
            context["header"] = "Amazing Finches"
        return context


class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'img', 'habitat', 'note', 'population', 'threat']
    template_name = "finch_create.html"

    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})


class FinchDetail(DetailView):
    model = Finch
    template_name = "finch_detail.html"


class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'img', 'habitat', 'note', 'population', 'threat']
    template_name = "finch_update.html"

    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})


class FinchDelete(DeleteView):
    model = Finch
    template_name = "finch_delete.html"
    success_url = "/finches/"


class About(TemplateView):
    template_name = 'about.html'


class SongCreate(View):
    def post(self, request, pk):
        title = request.POST.get("title")
        description = request.POST.get("description")
        # length = request.POST.get("length")
        audio = request.POST.get("audio")
        finch = Finch.objects.get(pk=pk)
        Song.objects.create(
            title=title, description=description, audio=audio, finch=finch)
        return redirect('finch_detail', pk=pk)
