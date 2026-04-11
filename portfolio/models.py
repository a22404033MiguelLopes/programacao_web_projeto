from django.db import models

# Create your models here.

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    ects = models.IntegerField()
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='licenciatura/', blank=True, null=True)

    def __str__(self):
        return self.nome
