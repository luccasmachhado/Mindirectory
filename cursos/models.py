from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='cursos/', blank=True, null=True)
    duracao = models.CharField(max_length=50, blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return super().__str__()