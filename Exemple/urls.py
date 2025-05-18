"""
URL configuration for Exemple project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('produits/', views.produits, name='produits'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),  
    path('exemple/', views.exemple, name='exemple'),
    path('services/flyers-carteVisite/', views.flyers_carteVisite, name='flyers_carteVisite'),
    path('services/site-vitrine/', views.service_site, name='service_site'),
    path('services/creation-affiches/', views.creation_affiche, name='creation_affiche'),
    path('recapitulatif/', views.recapitulatif_contact, name='recapitulatif_contact'),
    path('avis/', views.avis_view, name='avis'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


