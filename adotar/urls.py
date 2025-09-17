from django.urls import path
from adotar.views import *


urlpatterns = [
    path('', listar_pets, name='listar_pets'),
    path('solicitar_adocao/<int:id>/', solicitar_adocao, name='solicitar_adocao'),
] 
