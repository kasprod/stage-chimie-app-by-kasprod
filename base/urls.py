from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.index, name='home'),
    path('/actus', views.actus, name='actus'),
    path('/academy_team', views.academy_team, name='academy_team'),
    path('/meeting', views.meeting, name='meeting'),
]
       