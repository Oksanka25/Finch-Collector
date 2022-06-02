from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('finches/', views.FinchList.as_view(), name="finch_list"),
    path('finches/new/', views.FinchCreate.as_view(), name="finch_create"),
    path('finches/<int:pk>/', views.FinchDetail.as_view(), name="finch_detail"),
    path('finches/<int:pk>/update',
         views.FinchUpdate.as_view(), name="finch_update"),
    path('finches/<int:pk>/delete',
         views.FinchDelete.as_view(), name="finch_delete"),
    path('finches/<int:pk>/songs/new/',
         views.SongCreate.as_view(), name="song_create"),
    path('songs/<int:pk>/update',
         views.SongUpdate.as_view(), name="song_update"),
    path('songs/<int:pk>/delete',
         views.SongDelete.as_view(), name="song_delete"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")

]
