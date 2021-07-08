from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
       nombre = models.CharField(max_length=50)
       precio = models.FloatField()
       descripcion = models.TextField()
       categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
       imagen = models.ImageField(upload_to="productos", null=True)

       def __str__(self):
           return self.nombre

# class Carrito(models.Model):
#      usuario= models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario")
#      listaProductos= models.ManyToManyField(Producto)
    