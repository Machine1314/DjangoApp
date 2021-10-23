from django import forms
from .models import Integrante, Proyecto


class IntegranteForm(forms.ModelForm):
    class Meta:
        model = Integrante
        fields = ('codigo',
                  'nombre',
                  'apellido',
                  'usuario',
                  'contrasena')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            'contrasena': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        }


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('codigo',
                  'nombre',
                  'descripcion',
                  'tiempo_Estimado',
                  'costo_Estimado')
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Codigo'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
            'tiempo_Estimado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tiempo estimado'}),
            'costo_Estimado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '$'}),
             }
