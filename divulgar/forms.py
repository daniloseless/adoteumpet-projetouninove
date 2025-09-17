from divulgar.models import *
from django import forms

class CadastrarPet(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['especie', 'raca', 'nome', 'descricao',
                   'cidade', 'telefone', 'status', 'tag1', 'tag2',
                    'tag3', 'tag4', 'foto']
        
        widgets = {
            'especie': forms.Select(attrs={'class': 'form-control'}),
            'raca': forms.Select(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'status':forms.Select(attrs={'class': 'form-control'}),
            'tag1':forms.Select(attrs={'class': 'form-control'}),
            'tag2':forms.Select(attrs={'class': 'form-control'}),
            'tag3':forms.Select(attrs={'class': 'form-control'}),
            'tag4':forms.Select(attrs={'class': 'form-control'}),
            'foto':forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }