from django.db import models


# Create your models here.

class Catalogo(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    costo_Hora = models.FloatField(verbose_name="Costo por Hora")


class Proyecto(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60, default='')
    descripcion = models.CharField(max_length=500, verbose_name="Descripción", default='')
    tiempo_Estimado = models.FloatField(verbose_name="Tiempo Estimado en Semanas", default=0)
    tiempo_Actual = models.FloatField(default=0)
    costo_Estimado = models.FloatField(verbose_name="Costo por Estimado ($)", default=0)


class Integrante(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=50, verbose_name='Contraseña')
    capacidad = models.FloatField(verbose_name="Capacidad Integrante", default=0)
    rol = models.ForeignKey(Catalogo, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)


class Equipo(models.Model):
    codigo = models.IntegerField(max_length=4)
    nombre = models.CharField(max_length=100, default='')
    proyecto_Asociado = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE,
                                          verbose_name="Proyecto Asociado")
    integrante = models.ForeignKey(Integrante, null=True, blank=True, on_delete=models.CASCADE,
                                   verbose_name="Encargado")


class Historia(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60, default='')
    estado = models.ForeignKey(Catalogo, null=True, blank=True, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500, verbose_name="Descripción")
    complejidad = models.FloatField(verbose_name="Complejidad")
    proyecto_Asociado = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE,
                                          verbose_name="Proyecto Asociado")
    integrante_Encargado = models.ForeignKey(Integrante, null=True, blank=True, on_delete=models.CASCADE,
                                             verbose_name="Encargado")


class Tarea(models.Model):
    codigo = models.IntegerField(primary_key=True)
    historia_Asociada = models.ForeignKey(Historia, null=True, blank=True, on_delete=models.CASCADE,
                                          verbose_name="Historia Asociada")
    descripcion = models.CharField(max_length=500, verbose_name="Descripción")
    estado = models.ForeignKey(Catalogo, null=True, blank=True, on_delete=models.CASCADE)
    tiempo_Estimado = models.FloatField(verbose_name="Tiempo Estimado")
    tiempo_Real = models.FloatField(verbose_name="Tiempo Real Usado", null=True)
    integrante_Encargado = models.ForeignKey(Integrante, null=True, blank=True, on_delete=models.CASCADE,
                                             verbose_name="Encargado")


class Bug(models.Model):
    codigo = models.IntegerField(primary_key=True)
    historia_Asociada = models.ForeignKey(Historia, null=True, blank=True, on_delete=models.CASCADE,
                                          verbose_name="Historia Asociada")
    estado = models.ForeignKey(Catalogo, null=True, blank=True, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500, verbose_name="Descripción")
    integrante_Encargado = models.ForeignKey(Integrante, null=True, blank=True, on_delete=models.CASCADE,
                                             verbose_name="Encargado")
