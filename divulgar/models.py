from django.db import models
from django.contrib.auth.models import User

class Raca(models.Model):
    raca = models.CharField(max_length=120)

    def __str__(self):
        return self.raca


class Pet(models.Model):
    especies_escolhas = [('C', 'Cachorro'), ('G', 'Gato')]

    tag_escolhas = [
            ('Dócil', 'Dócil'),('Bravo', 'Bravo'),
            ('Carinhoso', 'Carinhoso'),('Manso', 'Manso'),
            ('Protetor', 'Protetor'),('Agitado', 'Agitado'),
            ('Vacinado', 'Vacinado'),('Castrado', 'Castrado'),
            ('Pelagem Longa', 'Pelagem Longa'), ('Especial', 'Especial'),
            ('Resgatado', 'Resgatado'), ('Pelagem Curta', 'Pelagem Curta'),
            ('Adestrado', 'Adestrado'), ('Hipoalergênico', 'Hipoalergênico'),
            ]
    
    status_escolhas = [('Adotado', 'Adotado'), ('Para adoção', 'Para adoção')]

    especie = models.CharField(choices=especies_escolhas, max_length=1)
    raca = models.ForeignKey(Raca, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=120)
    descricao = models.TextField()
    cidade = models.CharField(max_length=120)
    telefone = models.CharField(max_length=14)
    status = models.CharField(choices=status_escolhas, max_length=20, default='Para adoção')
    tag1 = models.CharField(max_length=120, choices=tag_escolhas, null=True, blank=True)
    tag2 = models.CharField(max_length=120, choices=tag_escolhas, null=True, blank=True)
    tag3 = models.CharField(max_length=120, choices=tag_escolhas, null=True, blank=True)
    tag4 = models.CharField(max_length=120, choices=tag_escolhas, null=True, blank=True)
    foto = models.ImageField(upload_to='pets')


    def __str__(self):
        return self.nome


