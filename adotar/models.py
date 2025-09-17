from django.db import models
from django.contrib.auth.models import User
from divulgar.models import Pet

# Create your models here.
class Pedido_Adocao(models.Model):
    status_escolhas = [
        ('AG', 'Aguardando Aprovacão'),
        ('AP', 'Aprovado'),
        ('RE', 'Rejeitado'),
    ]
    adotante = models.ForeignKey(User, on_delete=models.CASCADE)
    email_adotante = models.CharField(max_length=200, default='sememail@gmail.com')
    dono_pet = models.CharField(max_length=120, default='admin')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    data_solicitacao = models.DateTimeField()
    status_pedido = models.CharField(choices=status_escolhas, max_length=2, default='AG')

    def __str__(self):
        return f'PEDIDO! - O pet {self.pet} quer ser adotado por {self.adotante}'