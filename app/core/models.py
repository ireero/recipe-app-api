from django.db import models

class Imagem(models.Model):
    descricao = models.CharField(max_length=30)
    foto = models.ImageField()

    def __str__(self):
        return self.descricao
