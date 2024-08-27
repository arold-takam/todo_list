from django.db import models

class Tache(models.Model):  # Change 'tache' à 'Tache'
    titre = models.CharField(max_length=200)
    detail = models.TextField()
    day = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('draft', 'Brouillon'),
        ('published', 'Publier')
    ]
    statut = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.titre
