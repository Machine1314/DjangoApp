from django.db import models


# Create your models here.

class Rol(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    costo_Hora = models.FloatField(verbose_name="Costo por Hora")

    def __str__(self):
        return self.descripcion


class Estado(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class Equipo(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60, default='')
    descripcion = models.CharField(max_length=500, verbose_name="Descripción", default='')
    tiempo_Estimado = models.FloatField(verbose_name="Tiempo Estimado en Semanas", default=0)
    tiempo_Actual = models.FloatField(default=0)
    costo_Estimado = models.FloatField(verbose_name="Costo por Estimado ($)", default=0)
    equipo_Asociado = models.ForeignKey(Equipo, null=True, blank=True, on_delete=models.SET_NULL,
                                        verbose_name="Equipo Asociado")

    def __str__(self):
        return self.nombre


class Tiempos(models.Model):
    proyecto_id = models.IntegerField(null=False, blank=False)
    fecha = models.DateField(null=False)
    tiempo_Ideal = models.FloatField(null=False)
    tiempo_Actual = models.FloatField(null=True)


class Integrante(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    usuario = models.CharField(max_length=30, unique=True)
    contrasena = models.CharField(max_length=128, verbose_name='Contraseña')
    capacidad = models.FloatField(verbose_name="Capacidad Integrante", default=0)
    rol = models.ForeignKey(Rol, null=True, blank=True, on_delete=models.SET_NULL)
    equipo = models.ForeignKey(Equipo, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)


class Historia(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60, default='')
    estado = models.ForeignKey(Estado, null=True, blank=True, on_delete=models.SET_NULL)
    descripcion = models.CharField(max_length=500, verbose_name="Descripción")
    complejidad = models.FloatField(verbose_name="Complejidad")
    proyecto_Asociado = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE,
                                          verbose_name="Proyecto Asociado")
    integrante_Encargado = models.ForeignKey(Integrante, null=True, blank=True, on_delete=models.SET_NULL,
                                             verbose_name="Encargado")


class Tarea(models.Model):
    codigo = models.IntegerField(primary_key=True)
    historia_Asociada = models.ForeignKey(Historia, null=True, blank=True, on_delete=models.CASCADE,
                                          verbose_name="Historia Asociada")
    descripcion = models.CharField(max_length=500, verbose_name="Descripción")
    estado = models.ForeignKey(Estado, null=True, blank=True, on_delete=models.SET_NULL)
    tiempo = models.FloatField(verbose_name="Tiempo Restante")
    integrante_Encargado = models.ForeignKey(Integrante, null=True, blank=True, on_delete=models.SET_NULL,
                                             verbose_name="Encargado")


class Bug(models.Model):
    codigo = models.IntegerField(primary_key=True)
    historia_Asociada = models.ForeignKey(Historia, null=True, blank=True, on_delete=models.CASCADE,
                                          verbose_name="Historia Asociada")
    estado = models.ForeignKey(Estado, null=True, blank=True, on_delete=models.SET_NULL)
    descripcion = models.CharField(max_length=500, verbose_name="Descripción")
    integrante_Encargado = models.ForeignKey(Integrante, null=True, blank=True, on_delete=models.SET_NULL,
                                             verbose_name="Encargado")
