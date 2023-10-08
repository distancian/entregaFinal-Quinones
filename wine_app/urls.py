
from django.urls import path
from wine_app.views import eliminar_producto, editarPerfil, agregar_avatar, enviar_mensaje, page_not_found_view, detalles_producto, about, registrar, login_view, listarVendedores ,cliente, buscar, busquedaProducto, vendedor, producto, listar_clientes, listar_productos, listar_vendedores, inicio, agregar_producto, agregar_cliente, agregar_vendedor
from django.conf.urls import handler404
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import ProductoUpdateView, detalles_producto
from django.contrib.auth.views import LoginView
from .views import page_not_found_view


urlpatterns = [
    
    path('listar_clientes', listar_clientes, name='listar_clientes'),
    path('listar_productos', listar_productos, name='listar_productos'),
    path('listar_vendedores', listar_vendedores, name='listar_vendedores'),
    path('agregar_producto', agregar_producto, name='agregar_producto'),
    path('agregar_cliente', agregar_cliente, name='agregar_cliente'),
    path('agregar_vendedor', agregar_vendedor, name='agregar_vendedor'),
    path('busquedaProducto', busquedaProducto, name='busquedaProducto'),
    path('listarVendedores', listarVendedores, name='listarVendedores'),
    path('login', login_view, name= "Login"),
    path('registrar', registrar, name= "Registrar"),
    path('logout', LogoutView.as_view(template_name='logout.html'), name= "Logout"),
    path('about', about, name='about'),
    path('detalles_producto/<int:producto_id>/', detalles_producto, name='detalles_producto'),
    path('buscar', buscar, name='buscar'),
    path('inicio', inicio, name='inicio'),
    path('contacto', enviar_mensaje , name='contacto'),
    path('editar-perfil', editarPerfil , name='EditarPerfil'),
   
    path('Agregar-avatar', agregar_avatar , name='AgregarAvatar'),
    path('producto/editar/<int:pk>/', ProductoUpdateView.as_view(), name='editar_producto'),
    path('producto/detalles/<int:producto_id>/', detalles_producto, name='detalles_producto'),
    path('login2/', LoginView.as_view(), name='login2'),
    path('eliminar_producto/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),



]

handler404 = page_not_found_view

    


