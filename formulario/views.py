from django.shortcuts import render

from .models import Formulario

def lista_formularios(request):
    formularios = Formulario.objects.all()  # Recupera todos os formulários
    return render(request, 'formularios/lista.html', {'formularios': formularios})
