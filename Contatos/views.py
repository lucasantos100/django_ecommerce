from django.shortcuts import render

from .models import Contato

def contact_page(request):
    contact_form = Contato(request.POST or None)
    context = {
                    "title": "Contato - KGB Solutions",
                    "content": "Bem-Vindo à Página de Contato",
                    "form": contact_form	
              }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)


