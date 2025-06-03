from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
# This file defines the URL patterns for the base application of the Django project.
# It includes a single URL pattern that maps the root URL to the `index` view in the `views` module.        