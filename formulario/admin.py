from django.contrib import admin
from .models import Formulario

# Personalizando o título da barra de título do navegador
admin.site.site_header = 'KGB Solutions - Administração'

# Personalizando o título da página de login do admin
admin.site.site_title = 'Administração da KGB Solutions'

# Personalizando o título da página principal do admin
admin.site.index_title = 'Bem-vindo à administração da KGB Solutions'

admin.site.register(Formulario)