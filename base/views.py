from django.shortcuts import render
from .models import Actu, Professeur
from django.core.mail import send_mail
from django.conf import settings
from .models import RendezVous

# Create your views here.

def index(request):
    """
    Render the index page of the application.
    
    Args:
        request: The HTTP request object.
        
    Returns:
        HttpResponse: Rendered index page.
    """
    return render(request, 'base/pages/home.html')   

def actus(request):
    """
    Render the actus page with all actualités.
    """
    actus_list = Actu.objects.order_by('-date_pub')
    return render(request, 'base/pages/actus.html', {'actus_list': actus_list})

def academy_team(request):
    """
    Render the academy team page of the application.

    Args:
        request: The HTTP request object.
        
    Returns:
        HttpResponse: Rendered academy teams page.
    """
    professeurs = Professeur.objects.all()
    return render(request, 'base/pages/academy_team.html', {'professeurs': professeurs})


    

def meeting(request):
    """
    Gère la soumission du formulaire de rendez-vous et envoie une notification par e-mail à l'utilisateur.
    """
    if request.method == "POST":
        data = request.POST
        membre = data.get("membre")
        nom_autre = data.get("nom_autre") if membre == "autre" else ""
        poste_autre = data.get("poste_autre") if membre == "autre" else ""

        rdv = RendezVous.objects.create(
            nom_demandeur=data.get("nom_demandeur"),
            email_demandeur=data.get("email_demandeur"),
            domaine_demandeur=data.get("domaine_demandeur"),
            membre=membre,
            nom_autre=nom_autre,
            poste_autre=poste_autre,
            date=data.get("date"),
            heure=data.get("heure"),
            motif=data.get("motif"),
        )

        # Partie conditionnelle pour "autre"
        details_autre = ""
        if membre == "autre":
            details_autre = f"Nom autre : {rdv.nom_autre}\nPoste autre : {rdv.poste_autre}\n"

        # Message à l'utilisateur
        message_utilisateur = (
            f"Bonjour {rdv.nom_demandeur},\n\n"
            f"Votre demande de rendez-vous a bien été enregistrée.\n\n"
            f"Détails du rendez-vous :\n"
            f"Nom : {rdv.nom_demandeur}\n"
            f"Domaine : {rdv.domaine_demandeur}\n"
            f"Membre à rencontrer : {rdv.membre}\n"
            f"{details_autre}"
            f"Date : {rdv.date}\n"
            f"Heure : {rdv.heure}\n"
            f"Motif : {rdv.motif}\n\n"
            f"Nous vous contacterons pour confirmer ce rendez-vous.\n\n"
            f"Cordialement,\nDépartement de Chimie"
        )

        # Envoi à l'utilisateur
        send_mail(
            subject="Confirmation de votre rendez-vous - Département de Chimie",
            message=message_utilisateur,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[rdv.email_demandeur],
        )

        return render(request, "base/pages/rendez_vous.html", {"success": True})

    return render(request, "base/pages/rendez_vous.html")
