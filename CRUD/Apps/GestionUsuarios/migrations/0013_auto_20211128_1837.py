# Generated by Django 3.2.9 on 2021-11-28 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionUsuarios', '0012_auto_20211128_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='tiempo_Estimado',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='tiempo_Real',
        ),
        migrations.AddField(
            model_name='tarea',
            name='tiempo',
            field=models.FloatField(default=0, verbose_name='Tiempo Restante'),
            preserve_default=False,
        ),
    ]
