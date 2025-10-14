from django.urls import path
from adotar.views import *


urlpatterns = [
    path('', listar_pets, name='listar_pets'),
    path('meus_pedidos/', meus_pedidos, name='meus_pedidos'),
    path('cancelar_pedido/<int:id>/', cancelar_pedido, name='cancelar_pedido'),
    path('limpar_historico/', limpar_historico, name='limpar_historico'),
    path('solicitar_adocao/<int:id>/', solicitar_adocao, name='solicitar_adocao')
] 
