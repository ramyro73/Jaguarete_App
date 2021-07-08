from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
       list_display=["nombre", "precio" ,"descripcion","categoria"]
       

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)