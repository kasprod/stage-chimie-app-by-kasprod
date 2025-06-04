from django.db import models

class Actu(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='actus/')
    badge = models.CharField(max_length=50, default='Événement')
    badge_color = models.CharField(max_length=30, default='primary')
    date_pub = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Professeur(models.Model):
    nom = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profs/')
    domaine = models.CharField(max_length=200)
    publications = models.TextField(help_text="Séparez les publications par un saut de ligne")
    email = models.EmailField()

    def get_publications_list(self):
        return self.publications.split('\n')

    def __str__(self):
        return self.nom

class RendezVous(models.Model):
    nom_demandeur = models.CharField(max_length=100)
    email_demandeur = models.EmailField()
    domaine_demandeur = models.CharField(max_length=50)
    membre = models.CharField(max_length=100)
    nom_autre = models.CharField(max_length=100, blank=True, null=True)
    poste_autre = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    heure = models.TimeField()
    motif = models.CharField(max_length=255)
    date_demande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_demandeur} ({self.date} {self.heure})"