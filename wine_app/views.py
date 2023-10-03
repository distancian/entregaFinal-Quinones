from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Productos, Clientes, Vendedores, Avatar
from django.contrib import messages
from .forms import MensajeForm, UserEditForm, UserChangeForm, AvatarFormulario

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.



################### funciones  #########################

@login_required(login_url='/wine_app/login')
def cliente(req, nombre, apellido, dni, mail ):
    cliente = Clientes(nombre=nombre, apellido=apellido, dni=dni, mail=mail)
    cliente.save()
    return HttpResponse(f'''
    <p>Cliente: {cliente.nombre} - apellido: {cliente.apellido} creado con exito!</P>''')        

def producto(req, bodega, etiqueta, precio):
    producto = Productos(bodega=bodega, etiqueta=etiqueta, precio=precio)
    producto.delete()
    return HttpResponse(f'''
    <p>Bodega: {producto.bodega} - etiqueta: {producto.etiqueta} creado con exito!</P>''')  

@login_required(login_url='/wine_app/login')
def vendedor(req, nombre, apellido, legajo):
    vendedor = Vendedores(nombre=nombre, apellido=apellido, legajo=legajo)
    vendedor.save()
    return HttpResponse(f'''
    <p>Vendedor: {vendedor.nombre}{vendedor.apellido} creado con exito!</P>''')  

################### funciones agregar #########################

@login_required(login_url='/wine_app/login')
def agregar_producto(req):

    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        producto = Productos(bodega=req.POST["bodega"], etiqueta=req.POST["etiqueta"], precio=req.POST["precio"])
        producto.save()
        return render(req, "inicio.html")

    else:  
        return render(req, "agregar_producto.html")

@login_required(login_url='/wine_app/login')
def agregar_cliente(req):

    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        cliente = Clientes(nombre=req.POST["nombre"], apellido=req.POST["apellido"], dni=req.POST["dni"], mail=req.POST["mail"])
        cliente.save()
        return render(req, "inicio.html")

    else:  
        return render(req, "agregar_cliente.html")
    
@login_required(login_url='/wine_app/login')
def agregar_vendedor(req):

    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        vendedor = Vendedores(nombre=req.POST["nombre"], apellido=req.POST["apellido"], legajo=req.POST["legajo"])
        vendedor.save()
        return render(req, "inicio.html")

    else:  
        return render(req, "agregar_vendedor.html")
            
################### funciones listar #########################

def inicio(req):  
        
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req,"inicio.html", {"url_avatar": avatar.imagen.url})
    except:
        return render (req, "inicio.html")

@login_required(login_url='/wine_app/login')
def listar_clientes(req):
    lista = Clientes.objects.all()
    return render(req, "listar_clientes.html", {"listar_clientes": lista})

def listar_productos(req):
    lista = Productos.objects.all()
    return render(req, "listar_productos.html", {"listar_productos": lista})

@login_required(login_url='/wine_app/login')
def listar_vendedores(req):
    lista = Vendedores.objects.all()
    return render(req, "listar_vendedores.html", {"listar_vendedores": lista})


################### funciones busqueda  #########################

def busquedaProducto(req):
    return render (req, "busquedaProducto.html")

 
def buscar(req: HttpRequest):

    if req.GET["bodega"]:
        bodega = req.GET["bodega"]
        productob = Productos.objects.filter(bodega__icontains = bodega)
        return render(req, "resultadoBusqueda.html", {"bodega": productob})

    else:
        return HttpResponse (f'no existe..')
    
################### funciones listar  #########################

def listarVendedores(req):
    Vendedor = Vendedores.objects.all
    return render(req, "listarVendedores.html", {"Vendedores" : Vendedor})

################### funcion Login  #########################



def login_view (req):
    if req.method == "POST":
          
        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():
              
                data = miFormulario.cleaned_data
                usuario = data["username"]
                psw = data["password"]
                user = authenticate(username=usuario, password=psw)
                if user:
                    login(req, user)
                    return render(req, "inicio.html", {"mensaje": f'Bienvenido {usuario}!'})
        return render(req, "inicio.html", {"mensaje": f'Datos incorrectos'})
    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFormulario" : miFormulario})   

################### funcion Login  #########################


def registrar(req):
        if req.method == "POST":
          
                miFormulario = UserCreationForm(req.POST)

                if miFormulario.is_valid():
              
                    data = miFormulario.cleaned_data
                    usuario = data["username"]
                    miFormulario.save()
                    return render(req, "inicio.html", {"mensaje": f'{usuario} creado con exito'})   
                return render(req, "inicio.html", {"mensaje": f'Formulario incorrectos'})
        else:
            miFormulario = UserCreationForm()
            return render(req, "registrar.html", {"miFormulario" : miFormulario})   
        

################### funcion Login  #########################


def about(request):
    context = {
        'nombre': 'Tu Nombre',
        'experiencia': 'Más de 15 años en informática',
        'estudios': 'Estudiando programación en Python',
    }
    return render(request, 'about.html', context)

################### detalle producto  #########################

def detalles_producto(request, producto_id):
    producto = get_object_or_404(Productos, id=producto_id)
    return render(request, 'detalles_producto.html', {'producto': producto})

################### no existe  #########################

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

################### contactenos  #########################


def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Mensaje enviado correctamente.')
            return redirect('/wine_app/contacto')
    else:
        form = MensajeForm()

    return render(request, 'contacto.html', {'form': form})



############## editar perfil ###############

def editarPerfil(req):

    usuario = req.user

    if req.method == 'POST':
   
        miFormulario = UserEditForm(req.POST, instance=req.user)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()

            return render(req, "inicio.html", {"mensaje": "Datos actualizados con exito"})
        else:
            return render(req,"editarPerfil.html", {"miFormulario":miFormulario})        

    else:
        miFormulario = UserEditForm(instance=usuario)
        return render(req,"editarPerfil.html", {"miFormulario":miFormulario})        

############## agregar avatar ###############

def agregar_avatar(req):

    if req.method == 'POST':
   
        miFormulario = AvatarFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            avatar = Avatar(user=req.user, imagen=data["imagen"])
            avatar.save()
            return render(req,"inicio.html", {"mensaje": "avatar actualizado con exito"})        

    else:
        miFormulario = AvatarFormulario()
        return render(req,"agregarAvatar.html", {"miFormulario":miFormulario})    