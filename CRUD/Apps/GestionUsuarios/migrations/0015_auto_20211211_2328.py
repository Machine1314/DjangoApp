# Generated by Django 3.2.9 on 2021-12-11 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionUsuarios', '0014_auto_20211210_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='dias',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_inicio',
            field=models.DateField(null=True),
        ),
    ]
