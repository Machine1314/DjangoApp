# Generated by Django 3.0 on 2021-10-24 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestionUsuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='historia_Asociada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GestionUsuarios.Historia', verbose_name='Historia Asociada'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='historia_Asociada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GestionUsuarios.Historia', verbose_name='Historia Asociada'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='tiempo_Real',
            field=models.FloatField(null=True, verbose_name='Tiempo Real Usado'),
        ),
    ]
