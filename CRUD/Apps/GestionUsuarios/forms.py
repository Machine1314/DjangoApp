from django import forms
from .models import *


class IntegranteForm(forms.ModelForm):
    class Meta:
        model = Integrante
        fields = ('codigo',
                  'nombre',
                  'apellido',
                  'usuario',
                  'capacidad',
                  'rol',
                  'equipo',
                  'contrasena')
        widgets = {
            'codigo': forms.HiddenInput(),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'capacidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Capacidad'}),
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            'contrasena': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}, render_value = True),
            'rol': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Escoge'},
                                                 choices=Rol.objects.all().values_list('codigo', 'descripcion')),
            'equipo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Escoge'},
                                choices=Equipo.objects.all().values_list('codigo', 'nombre')),
        }


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ('codigo',
                  'nombre',
                  'proyecto_Asociado')

        widgets = {
            'codigo': forms.HiddenInput(),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Equipo'}),\
            'proyecto_Asociado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Escoge'},
                                                 choices=Proyecto.objects.all().values_list('codigo', 'nombre')),
        }

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ('codigo',
                  'descripcion',
                  'costo_Hora')

        widgets = {
            'codigo': forms.HiddenInput(),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'costo_Hora': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Costo en $ por hora'}),
        }


class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ('codigo',
                  'descripcion')

        widgets = {
            'codigo': forms.HiddenInput(),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
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
            'codigo': forms.HiddenInput(),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
            'tiempo_Estimado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tiempo estimado'}),
            'costo_Estimado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '$'}),
        }


class HistoriaForm(forms.ModelForm):
    class Meta:
        model = Historia
        fields = ('codigo',
                  'nombre',
                  'estado',
                  'descripcion',
                  'complejidad',
                  'proyecto_Asociado',
                  'integrante_Encargado')
        widgets = {
            'codigo': forms.HiddenInput(),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'estado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Escoge'},
                                   choices=Estado.objects.all().values_list('codigo', 'descripcion')),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
            'complejidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Complejidad'}),
            'proyecto_Asociado': forms.HiddenInput(),
            'integrante_Encargado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Escoge'},
                                                 choices=Integrante.objects.all().values_list('codigo', 'apellido')),
        }


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ('codigo',
                  'historia_Asociada',
                  'descripcion',
                  'estado',
                  'tiempo_Estimado',
                  'integrante_Encargado')
        widgets = {
            'codigo': forms.HiddenInput(),
            'historia_Asociada': forms.HiddenInput(),
            'estado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Escoge'},
                                   choices=Estado.objects.all().values_list('codigo', 'descripcion')),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
            'complejidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Complejidad'}),
            'tiempo_Estimado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tiempo en horas'}),
            'integrante_Encargado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Escoge'},
                                                 choices=Integrante.objects.all().values_list('codigo', 'apellido')),
        }


class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('codigo',
                  'historia_Asociada',
                  'descripcion',
                  'estado',
                  'integrante_Encargado')
        widgets = {
            'codigo': forms.HiddenInput(),
            'historia_Asociada': forms.HiddenInput(),
            'estado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Escoge'},
                                   choices=Estado.objects.all().values_list('codigo', 'descripcion')),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
            'integrante_Encargado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Escoge'},
                                                 choices=Integrante.objects.all().values_list('codigo', 'apellido')),
        }
