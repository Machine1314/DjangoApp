from django.db import models


# Create your models here.
class Usuario(models.Model):
    codigo = models.CharField(max_length=6)
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    FechaNacimiento = models.DateField()
    Usuario = models.CharField(max_length=40)
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')
    Contrasena = models.CharField(max_length=20)

    def Datos(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.Apellido, self.Nombre, self.Usuario)

    def __str__(self):
        return self.Datos()
