from django.db import models

class Estudantes(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
