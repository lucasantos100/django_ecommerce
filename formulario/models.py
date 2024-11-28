from django.db import models
from django.utils import timezone

class Formulario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15, null=True)  
    data = models.DateField(default=timezone.now)  
    horario = models.TimeField(default="08:00:00")
    mensagem = models.TextField()

    def __str__(self):
        return self.nome