from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
# This will import the class we are extending
from django.views.generic.edit import CreateView

# import models
from .models import Finch


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
    success_url = "/finches/"


class About(TemplateView):
    template_name = 'about.html'


class Index(TemplateView):
    template_name = 'index.html'
