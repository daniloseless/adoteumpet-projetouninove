from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from divulgar.models import *
from divulgar.forms import *
from adotar.models import *

# Create your views here.

@login_required
def cadastrar_pet(request):
    if request.method == 'GET':
        form = CadastrarPet()
        return render(request, 'cadastrar_pets.html', {'form':form})
    
    elif request.method == 'POST':
        form = CadastrarPet(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.usuario = request.user
            pet.save()
            messages.add_message(request, constants.SUCCESS, 'Pet cadastrado com sucesso!')
            return render(request, 'cadastrar_pets.html')
        else:
            messages.add_message(request, constants.ERROR, 'Não foi possivel cadastrar, verifique os dados')
            return render(request, 'cadastrar_pets.html', {'form':form})


@login_required
def seus_pets(request):
    if request.method == 'GET':
        pets = Pet.objects.filter(usuario=request.user)
        return render(request, 'seus_pets.html', {'pets': pets})
    

@login_required
def detalhar_pet(request, id):
    if request.method == 'GET':
        pets = Pet.objects.filter(id=id)
        return render(request, 'detalhar_pet.html', {'pets': pets})
    

@login_required
def remover_pet(request, id):
    pet = Pet.objects.get(pk=id)
    if pet.usuario == request.user:
        pet.delete()
        pets = Pet.objects.filter(usuario=request.user)
        messages.add_message(request, constants.WARNING, 'Pet removido com sucesso!')
        return render(request, 'seus_pets.html', {'pets': pets})
    else:
        pets = Pet.objects.filter(usuario=request.user)
        messages.add_message(request, constants.ERROR, 'Voce só pode remover seus Pets!')
        return render(request, 'seus_pets.html', {'pets': pets})
    

@login_required
def pedidos(request):
    if request.method == 'GET':
        pedidos = Pedido_Adocao.objects.filter(status_pedido='AG').filter(dono_pet=request.user)
        return render(request, 'pedidos.html', {'pedidos': pedidos})
    
@login_required
def processar_pedido(request, id):
    status = request.GET.get('status')
    pedido = Pedido_Adocao.objects.get(id=id)
    pet = Pet.objects.get(id=pedido.pet.id)
   
    if status == 'Aprovado':
        pedido.status_pedido = 'AP'
        pet.status = 'Adotado'
        pet.save()
    
    if status == 'Recusado':
        pedido.status_pedido = 'RE'
        
    pedido.save()

    return redirect('/adotar')