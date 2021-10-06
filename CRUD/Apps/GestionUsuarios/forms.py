from django import forms
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('codigo',
                  'Nombre',
                  'Apellido',
                  'Usuario',
                  'Sexo',
                  'Contrasena',
                  'FechaNacimiento')
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'Apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'Usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            'Sexo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Sexo'}),
            'Contrasena': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
            'FechaNacimiento': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Selecciona una fecha',
                       'type': 'date'
                       }),
        }
