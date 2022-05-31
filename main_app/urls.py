from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('index/', views.Index.as_view(), name="index"),
    path('finches/', views.FinchList.as_view(), name="finch_list"),
    path('finches/new/', views.FinchCreate.as_view(), name="finch_create")
]
