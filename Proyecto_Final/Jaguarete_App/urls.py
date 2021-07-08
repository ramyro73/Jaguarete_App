from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
       # path('saludar/<str:nombre>', views.saludar, name="saludar"),
       # path('menu', views.menu, name="menu")
       # path('header', views.header, name="header"),
       path('acerca', views.acerca, name="acerca"),
       path('altaProd', views.altaProd, name="altaProd"),
       # path('agregarProd', views.agregarProd, name="agregarProd"),
       path('contacto', views.contacto, name="contacto"),
       path('home', views.home, name="home"),
       # path('base', views.base, name="base"),
       path('producto/<int:id>', views.producto, name="producto"),
       path('editProd/<int:id>', views.editProd, name="editProd"),
       path('editarProd/<id>/', views.editarProd, name="editarProd"),
       path('eliminarProd/<id>/', views.eliminarProd, name="eliminarProd"),
       path('login', views.login, name="login"),
       path('registro', views.registro, name="registro"),
       # path('carrito', views.carrito, name="carrito"),
       path('buscar', views.buscar, name="buscar"),
       path('filtroCategoria/<int:categoria_id>', views.filtroCategoria, name="filtroCategoria"),
       

       path("agregar/<int:producto_id>/", views.agregarProducto, name="agregar"),
       path("eliminar/<int:producto_id>/", views.eliminarProducto, name="eliminar"),
       path("restar/<int:producto_id>/", views.restarProducto, name="restar"),
       path("limpiar/", views.limpiarCarrito, name="limpiar"),
       path("carrito/", views.carrito, name="carrito"),
       

]
#     path('', views., name=""),
# path('nuevo', views.nuevo, name="nuevo"),
# path('heladeras', views.heladeras, name="heladeras"),
# path('lavarropas', views.lavarropas, name="lavarropas"),
#  path('televisores', views.televisores, name="televisores"),
# path('bodyHome', views.bodyHome, name="bodyHome"),