# Generated by Django 3.2.9 on 2021-11-18 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpedidos', '0002_alter_clientes_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.CharField(max_length=7, verbose_name='contacto'),
        ),
    ]
