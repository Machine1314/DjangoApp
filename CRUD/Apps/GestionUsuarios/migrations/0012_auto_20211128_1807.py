# Generated by Django 3.2.9 on 2021-11-28 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionUsuarios', '0011_alter_tiempos_proyecto_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tiempos',
            old_name='fecha_Ideal',
            new_name='fecha',
        ),
        migrations.RemoveField(
            model_name='tiempos',
            name='fecha_Actual',
        ),
    ]