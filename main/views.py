from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings

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

