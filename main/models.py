from django.db import models

class Avis(models.Model):
    nom = models.CharField(max_length=100)
    commentaire = models.TextField()
    note = models.IntegerField(choices=[(i, f"{i} étoile{'s' if i > 1 else ''}") for i in range(1, 6)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.note}★"
