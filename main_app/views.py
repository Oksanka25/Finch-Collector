from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.shortcuts import redirect
from django.views import View
# Authorization
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Authentication
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from .models import Finch, Song


class Home(TemplateView):
    template_name = 'home.html'


@method_decorator(login_required, name='dispatch')
class FinchList(TemplateView):
    template_name = "finch_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["finches"] = Finch.objects.filter(
                name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["finches"] = Finch.objects.filter(user=self.request.user)
            context["header"] = "Amazing Finches"
        return context


@method_decorator(login_required, name='dispatch')
class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'img', 'habitat', 'note', 'population', 'threat']
    template_name = "finch_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FinchCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class FinchDetail(DetailView):
    model = Finch
    template_name = "finch_detail.html"


@method_decorator(login_required, name='dispatch')
class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'img', 'habitat', 'note', 'population', 'threat']
    template_name = "finch_update.html"

    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class FinchDelete(DeleteView):
    model = Finch
    template_name = "finch_delete.html"
    success_url = "/finches/"


class About(TemplateView):
    template_name = 'about.html'


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class SongUpdate(UpdateView):
    model = Song
    fields = ['title', 'description', 'audio']
    template_name = "song_update.html"

    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.finch_id})


@method_decorator(login_required, name='dispatch')
class SongDelete(DeleteView):
    model = Song
    template_name = "song_delete.html"

    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.finch_id})


class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("finch_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
