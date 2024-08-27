from django.contrib import admin
from .models import Tache  # Change 'tache' à 'Tache' pour correspondre au modèle

# Register your models here.
class TacheAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'statut', 'day')  # Champs affichés dans la vue liste
    list_filter = ('statut',)  # Filtrer par statut
    search_fields = ('id', 'titre', 'detail', 'day')  # Rechercher par ID, titre, détail et date

admin.site.register(Tache, TacheAdmin)  # Enregistre Tache avec sa configuration d'administration
