from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=7, verbose_name='contacto')
    def __str__(self):
        return 'nombre: %s , direccion: %s , email: %s telefono: %s' %(self.nombre, self.direccion, self.email, self.telefono)
class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()
    def __str__(self):
        return 'nombre: %s , seccion: %s , precio: %s' %(self.nombre, self.seccion, self.precio)
class pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
