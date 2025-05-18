from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Avis
from .forms import AvisForm
from django.contrib import messages


def index(request):
    return render(request, 'main/index.html')

def produits(request):
    return render(request, 'main/produits.html')

def services(request):
    return render(request, 'main/services.html')

def exemple(request):
    return render(request, 'main/exemple.html')

def service_site(request):
    return render(request, 'main/service_site.html')

def creation_affiche(request):
    return render(request, 'main/creation_affiche.html')

def flyers_carteVisite(request):
    return render(request, 'main/flyers_carteVisite.html')

def contact(request):
    if request.method == "POST":
        nom = request.POST.get("nom")
        email = request.POST.get("email")
        service = request.POST.get("service")
        details = request.POST.get("details")

        sujet = f"[Demande de contact] {service} - {nom}"
        message = f"Nom : {nom}\nEmail : {email}\nService souhaité : {service}\n\nDétails :\n{details}"
        destinataire = [settings.EMAIL_HOST_USER]

        email_message = EmailMessage(
            subject=sujet,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=destinataire
        )
        email_message.content_subtype = "plain"
        email_message.encoding = "utf-8"
        email_message.send()

        # 👉 Enregistre les infos dans la session pour les afficher ensuite
        request.session['nom'] = nom
        request.session['email'] = email
        request.session['service'] = service
        request.session['details'] = details

        return redirect("recapitulatif_contact")

    return render(request, "main/contact.html")

def recapitulatif_contact(request):
    context = {
        'nom': request.session.get('nom'),
        'email': request.session.get('email'),
        'service': request.session.get('service'),
        'details': request.session.get('details'),
    }
    return render(request, "main/recapitulatif.html", context)

def avis_view(request):
    note_filter = request.GET.get('note')
    avis_liste = Avis.objects.all().order_by('-date')
    if note_filter:
        avis_liste = avis_liste.filter(note=note_filter)

    if request.method == 'POST':
        form = AvisForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Merci pour votre avis !")
            return redirect('avis')
    else:
        form = AvisForm()

    return render(request, 'main/avis.html', {
        'form': form,
        'avis_liste': avis_liste,
        'note_filter': note_filter,
    })

def home_view(request):
    derniers_avis = Avis.objects.all().order_by('-date')[:3]
    return render(request, 'main/home.html', {'derniers_avis': derniers_avis})

