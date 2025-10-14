# divulgar/forms.py

from divulgar.models import *
from django import forms

class CadastrarPet(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['foto', 'nome', 'descricao', 'especie', 'raca', 'cidade', 'telefone', 'tag1', 'tag2', 'tag3', 'tag4']
        
        
        labels = {
            'tag1': 'Característica 1',
            'tag2': 'Característica 2',
            'tag3': 'Característica 3',
            'tag4': 'Característica 4',
        }

        widgets = {
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do pet'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva um pouco sobre a história e personalidade do pet', 'rows': 3}),
            'especie': forms.Select(attrs={'class': 'form-control'}),
            'raca': forms.Select(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: São Paulo'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(__) _____-____'}),
            'tag1': forms.Select(attrs={'class': 'form-control'}),
            'tag2': forms.Select(attrs={'class': 'form-control'}),
            'tag3': forms.Select(attrs={'class': 'form-control'}),
            'tag4': forms.Select(attrs={'class': 'form-control'}),
        }