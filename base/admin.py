from django.contrib import admin
from .models import Actu, Professeur

# Register your models here.
admin.site.site_header = "Projet Group 4 Admin"
admin.site.site_title = "Projet Group Four Admin Portal"
admin.site.index_title = "Welcome to the Projet Group Four Admin Portal"

# Register models
admin.site.register(Actu)
admin.site.register(Professeur)