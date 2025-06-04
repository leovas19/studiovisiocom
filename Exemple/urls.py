from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views
from main.views import suivi_projet, admin_projets, logout_view, redirect_after_login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.intro_view, name='intro'),     # Page d'intro affichée à /
    path('accueil/', views.index, name='index'),  # ou autre chemin selon ta structure    path('produits/', views.produits, name='produits'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('exemple/', views.exemple, name='exemple'),
    path('services/flyers-carteVisite/', views.flyers_carteVisite, name='flyers_carteVisite'),
    path('services/site-vitrine/', views.service_site, name='service_site'),
    path('services/creation-affiches/', views.creation_affiche, name='creation_affiche'),
    path('recapitulatif/', views.recapitulatif_contact, name='recapitulatif_contact'),
    path('avis/', views.avis_view, name='avis'),
    path('services/solutions-ia/', views.solutions_ia, name='solutions_ia'),
    path('services/marketing/', views.marketing_digital, name='marketing_digital'),
    path('services/design-graphique/', views.design_graphique, name='design_graphique'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/la-table-antoine/', views.projet_la_table_antoine, name='projet_la_table_antoine'),
    path('portfolio/axel-designs/', views.axel_designs, name='axel_designs'),
    path('portfolio/elegance-spa/', views.elegance_spa, name='elegance_spa'),
    path('a-propos/', views.about, name='about'),
    path('mon-compte/', suivi_projet, name='suivi_projet'),
    path('admin-projets/', admin_projets, name='admin_projets'),
    path('post-login/', redirect_after_login, name='post_login'),
    path("confidentialite/", views.politique_confidentialite, name="politique_confidentialite"),
    path("conditions/", views.conditions_utilisation, name="conditions_utilisation"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='main/login_client.html'), name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('post-login/', redirect_after_login, name='post_login'),
]


