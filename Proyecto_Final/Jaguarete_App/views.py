from django.contrib.auth.backends import UserModel
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse

from Jaguarete_App.carrito import Carrito


from .models import Categoria, Producto
from django.db.models import Q
from .forms import CustomUserCreationForm, ProductoForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.

def acerca(request):
       categorias= Categoria.objects.all()
       data={
       
              'categoria':categorias
       }
       return render(request,"acerca.html", data) 


# def altaProd(request):
       
#        categorias= Categoria.objects.all()
       
#        return render(request,"altaProd.html", {'categoria':categorias}) 

def altaProd(request):

       categorias= Categoria.objects.all()
       data ={
              'form': ProductoForm(),
              'categoria':categorias
       }

       if request.method == 'POST':
              formulario= ProductoForm(data=request.POST, files=request.FILES)
              if formulario.is_valid():
                     formulario.save()
              else:
                     data["form"]= formulario


       return render(request,"altaProd.html", data) 

def contacto(request):
       categorias= Categoria.objects.all()
       data={
       
              'categoria':categorias
       }
       return render(request,"contacto.html", data) 
 

       
def home (request):
       productos = Producto.objects.all()
       categorias= Categoria.objects.all()
       data={
              'productos': productos,
              'categoria':categorias
       }

       return render(request,"home.html", data) 

# def bodyHome (request):
#        return render(request,"bodyHome.html", {}) 

def producto(request, id):
       categorias= Categoria.objects.all()
       
       producto = Producto.objects.get(id=id)
       return render(request, "producto.html",{
              'producto':producto,
              'categoria':categorias
       })

def editProd(request,id):

       un_prod = get_object_or_404(Producto, id=id)
       if request.method == "POST":  
              user = UserModel.objects.get(username=request.user)   
              un_prod.publicador = user
              form = ProductoForm(data=request.POST, files=request.FILES, instance=un_prod)
              if form.is_valid():
                     form.save()
                     return redirect("home")
       else:
              form = ProductoForm(instance = un_prod)
              return render(request, 'producto/articulo_edicion.html', {
              "articulo": un_prod,
              "form": form
              })


def editarProd(request, id):
       categorias= Categoria.objects.all()
       

       producto= get_object_or_404(Producto, id=id)

       if request.method=="POST":
              form= ProductoForm(request.POST, instance=producto)
              if form.is_valid():
                     form.save()
                     return render(request, "home.html", {})
       else:
              form= ProductoForm(instance=producto)
              return render(request,"producto/editar.html", {
                     "producto": producto,
                     "form": form,
                     'categoria':categorias
              }) 


def eliminarProd(request, id):

       un_producto = get_object_or_404(Producto, id=id)
       un_producto.delete()
       return redirect("home")


def registro(request):
       categorias= Categoria.objects.all()
      
       data = {
              'form': CustomUserCreationForm(),
              'categoria':categorias
       }

       if request.method == 'POST':
              formulario = CustomUserCreationForm(data=request.POST)
              if formulario.is_valid():
                     formulario.save()
                     user= authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
                     login(request, user)
                     return redirect(to="home")
              data["form"] = formulario

       return render(request, "registration/registro.html",data)   


def buscar(request):
       # mensaje = "articulo buscado: %r" %request.GET["prod"]

       if request.GET.get("prod"):
              busqueda = request.GET.get("prod")

              productos = Producto.objects.filter(
                     Q(nombre__icontains= busqueda)|
                     Q(descripcion__icontains = busqueda)
              ).distinct

              return render(request, "buscarProd.html",{'productos': productos, 'query': busqueda}) 
       else:
              mensaje="no has introducido nada"

       return render(request, "buscarProd.html",{'mensaje':mensaje})   

       # return HttpResponse(mensaje)

def filtroCategoria(request, categoria_id):
    categorias= Categoria.objects.all()
    una_categoria = get_object_or_404(Categoria, id=categoria_id)
    queryset = Producto.objects.all()
    queryset = queryset.filter(categoria=una_categoria)
    return render(request,"buscarProd.html", {
        "listaProductos": queryset,
        "listaCategorias": Categoria.objects.all(),
        'categoria':categorias,
        "categoriaSeleccionada": una_categoria
    })






def agregarProducto(request, producto_id):

       carrito=Carrito(request)

       producto = Producto.objects.get(id=producto_id)

       carrito.agregar(producto=producto)

       return redirect("carrito")

def eliminarProducto(request, producto_id):

       carrito=Carrito(request)

       producto = Producto.objects.get(id=producto_id)

       carrito.eliminar(producto= producto)

       return redirect("carrito")

def restarProducto(request, producto_id):

       carrito=Carrito(request)

       producto = Producto.objects.get(id=producto_id)

       carrito.restar_producto(producto= producto)

       return redirect("carrito")

def limpiarCarrito(request):

       carrito=Carrito(request)

       carrito.limpiar_carrito()

       return redirect("home")

def carrito(request):
       categorias= Categoria.objects.all()
       data={
       
              'categoria':categorias
       }
       # producto = Producto.objects.all()
       return render(request, "carrito.html",data)   



