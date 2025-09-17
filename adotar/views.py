from django.shortcuts import render, HttpResponse, redirect
from divulgar.models import *
from adotar.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime

# Create your views here.
@login_required
def listar_pets(request):
    if request.method == 'GET':
        pets = Pet.objects.all()
        racas = Raca.objects.all()

        cidade = request.GET.get('cidade')
        raca_filtro = request.GET.get('raca')

        if cidade != None:
            pets = pets.filter(cidade__icontains=cidade)

        if raca_filtro:
            pets= pets.filter(raca=raca_filtro) 
        
        return render(request, 'listar_pets.html', {'pets':pets, 'racas':racas})

    
@login_required
def solicitar_adocao(request, id):
    pet = Pet.objects.filter(pk=id).filter(status='Para adoção')

    if not pet.exists():
        messages.add_message(request, constants.ERROR, 'O Pet não está disponível')
        return render(request, 'listar_pets.html' )
    else:
        usuario_dono = ''

        for i in pet:
            usuario_dono = i.usuario  # vai buscar o dono do pet via queryset

        pedido = Pedido_Adocao(
            pet = pet.first(),
            dono_pet = usuario_dono,
            adotante = request.user,
            email_adotante = request.user.email,
            data_solicitacao = datetime.now(),)

        pedido.save()
        messages.add_message(request, constants.SUCCESS, 'Pedido realizado com sucesso!')
        return redirect('/adotar')


        
