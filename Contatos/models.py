from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15, null=True, blank=True)  # Adicionando blank=True para ser opcional
    data = models.DateField()
    horario = models.TimeField()
    mensagem = models.TextField()

    def __str__(self):
        return self.nome