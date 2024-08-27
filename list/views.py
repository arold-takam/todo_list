from django.shortcuts import render, redirect
from .forms import TacheForm
from .models import Tache
from django.shortcuts import get_object_or_404


def home(request):
    taches=Tache.objects.all()
    return render(request, 'home.html', {'taches': taches})

def Add_Task(request):
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarde la tâche
            return redirect('home')  # Redirige vers la page d'accueil ou une autre page
    else:
        form = TacheForm()

    return render(request, 'Add_Task.html', {'form': form})

def detail(request, id):
    tache = get_object_or_404(Tache, id=id)  # Récupère la tâche par son ID ou retourne une erreur 404 si non trouvée
    return render(request, 'detail.html', {'tache': tache})

def Modify_Task(request, id):
    tache = get_object_or_404(Tache, id=id)
    
    if request.method == 'POST':
        form = TacheForm(request.POST, instance=tache)
        if form.is_valid():
            form.save()
            return redirect('detail', id=tache.id)  # Redirige vers la page de détail après modification
    else:
        form = TacheForm(instance=tache)  # Pré-remplit le formulaire avec les informations actuelles de la tâche
    
    return render(request, 'Modify_Task.html', {'form': form, 'tache': tache})