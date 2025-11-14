from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='cursos/', blank=True, null=True)
    duracao = models.CharField(max_length=50, blank=True)
    nivel = models.CharField(max_length=50, blank=True)
    professor = models.CharField(max_length=50, blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    modulos = models.JSONField(default=list, blank=True)


    def __str__(self):
        return super().__str__()
    
