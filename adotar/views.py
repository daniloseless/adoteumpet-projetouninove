from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from divulgar.models import *
from adotar.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime

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

@login_required
def meus_pedidos(request):
    if request.method == "GET":
        # Filtra os pedidos de adoção onde o 'adotante' é o usuário logado
        pedidos = Pedido_Adocao.objects.filter(adotante=request.user)
        return render(request, 'meus_pedidos.html', {'pedidos': pedidos})

@login_required
def cancelar_pedido(request, id):
    pedido = get_object_or_404(Pedido_Adocao, id=id)

    if not pedido.adotante == request.user:
        messages.add_message(request, constants.ERROR, 'Este pedido não é seu!')
        return redirect('/adotar/meus_pedidos/')

    if not pedido.status_pedido == 'AG':
        messages.add_message(request, constants.WARNING, 'Este pedido já foi processado e não pode ser cancelado.')
        return redirect('/adotar/meus_pedidos/')

    pedido.delete()
    messages.add_message(request, constants.SUCCESS, 'Pedido de adoção cancelado com sucesso.')
    return redirect('/adotar/meus_pedidos/')

@login_required
def limpar_historico(request):
    if request.method == "POST":

        pedidos_concluidos = Pedido_Adocao.objects.filter(adotante=request.user).filter(
            status_pedido__in=['AP', 'RE']
        )
        pedidos_concluidos.delete()
        messages.add_message(request, constants.SUCCESS, 'Histórico de pedidos limpo com sucesso.')
        return redirect('meus_pedidos')
    else:
        return redirect('meus_pedidos')
