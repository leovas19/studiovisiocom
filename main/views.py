from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Avis, Projet
from .forms import AvisForm
from django.http import HttpResponseRedirect

# ==========================
#  ADMIN DASHBOARD PROJETS
# ==========================

STATUTS = ['En attente', 'En cours', 'En design', 'Développement', 'Terminé']

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def admin_projets(request):
    projets = Projet.objects.select_related('client').all().order_by('-date_creation')
    users = User.objects.all()

    if request.method == "POST":
        if 'ajout_projet' in request.POST:
            user_id = request.POST.get("client_id")
            nom_projet = request.POST.get("nom_projet")
            statut_initial = request.POST.get("statut_initial")

            if user_id and nom_projet:
                try:
                    client = User.objects.get(id=user_id)
                    Projet.objects.create(client=client, nom=nom_projet, statut=statut_initial)
                    messages.success(request, f"Projet '{nom_projet}' ajouté pour {client.username}.")
                except User.DoesNotExist:
                    messages.error(request, "Utilisateur introuvable.")
            else:
                messages.error(request, "Tous les champs doivent être remplis.")

        elif 'maj_projet' in request.POST:
            projet_id = request.POST.get("projet_id")
            nouveau_statut = request.POST.get("statut")
            message_client = request.POST.get("message_client")
        
            try:
                projet = Projet.objects.get(id=projet_id)
                projet.statut = nouveau_statut
                projet.message_client = message_client  # ✅ mise à jour du message
                projet.save()
                messages.success(request, f"Statut et message du projet '{projet.nom}' mis à jour.")
            except Projet.DoesNotExist:
                messages.error(request, "Projet introuvable.")


        elif 'delete_projet_id' in request.POST:
            projet_id = request.POST.get("delete_projet_id")
            try:
                projet = Projet.objects.get(id=projet_id)
                projet.delete()
                messages.success(request, f"Projet '{projet.nom}' supprimé.")
            except Projet.DoesNotExist:
                messages.error(request, "Projet introuvable pour suppression.")

        return redirect('admin_projets')

    return render(request, 'main/admin_projets.html', {
        'projets': projets,
        'statuts': STATUTS,
        'users': users,
    })




# ==========================
#       PROJETS CLIENTS
# ==========================

@login_required
def suivi_projet(request):
    projets = Projet.objects.filter(client=request.user)

    # Si un message est en session, le transférer à messages
    if 'flash_message' in request.session:
        messages.success(request, request.session.pop('flash_message'))

    return render(request, 'main/suivi_projet.html', {'projets': projets})


# ==========================
#         CONTACT
# ==========================

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

        request.session['nom'] = nom
        request.session['email'] = email
        request.session['service'] = service
        request.session['details'] = details
        messages.success(request, "Votre message a bien été envoyé ! Nous vous répondrons sous 24h.")
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

# ==========================
#          AVIS
# ==========================

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

# ==========================
#        PAGES PUBLIQUES
# ==========================

def intro_view(request):
    return render(request, 'main/intro.html')

def index(request):
    derniers_avis = Avis.objects.order_by('-date')[:3]
    return render(request, 'main/index.html', {'derniers_avis': derniers_avis})

def about(request):
    return render(request, 'main/about.html')

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

def solutions_ia(request):
    return render(request, 'main/solutions-ia.html')

def marketing_digital(request):
    return render(request, 'main/marketing-digital.html')

def design_graphique(request):
    return render(request, 'main/design-graphique.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def projet_la_table_antoine(request):
    return render(request, 'main/projets/la-table-antoine.html')

def axel_designs(request):
    return render(request, 'main/axel-designs.html')

def elegance_spa(request):
    return render(request, 'main/elegance-spa.html')

# ==========================
#      AUTHENTIFICATION
# ==========================

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Vous avez bien été déconnecté(e).")
    return redirect('/')

@login_required
def redirect_after_login(request):
    if request.user.is_superuser:
        messages.success(request, "Connexion administrateur réussie ✅")
        return HttpResponseRedirect('/admin-projets/')
    else:
        messages.success(request, "Connexion utilisateur réussie ✅")
        return HttpResponseRedirect('/mon-compte/')

# ==========================
#      CONDITION
# ==========================

def politique_confidentialite(request):
    return render(request, 'main/politique_confidentialite.html')

def conditions_utilisation(request):
    return render(request, 'main/conditions_utilisation.html')
