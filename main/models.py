from django.db import models
from django.contrib.auth.models import User

class Avis(models.Model):
    nom = models.CharField(max_length=100)
    commentaire = models.TextField()
    note = models.IntegerField(choices=[(i, f"{i} étoile{'s' if i > 1 else ''}") for i in range(1, 6)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.note}★"


class Projet(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    statut = models.CharField(
        max_length=50,
        choices=[
            ('En attente', 'En attente'),
            ('En cours', 'En cours'),
            ('En design', 'Design en cours'),
            ('Développement', 'Développement'),
            ('Terminé', 'Terminé'),
        ],
        default='En attente'
    )
    date_creation = models.DateTimeField(auto_now_add=True)
    message_client = models.TextField(blank=True, null=True)  # ✅ nouveau champ

    def __str__(self):
        return f"{self.nom} ({self.client.username})"
