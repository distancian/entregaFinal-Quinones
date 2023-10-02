
from django.urls import path
from wine_app.views import editarPerfil, enviar_mensaje, page_not_found_view, detalles_producto, about, registrar, login_view, listarVendedores ,cliente, buscar, busquedaProducto, vendedor, producto, listar_clientes, listar_productos, listar_vendedores, inicio, agregar_producto, agregar_cliente, agregar_vendedor
from django.conf.urls import handler404
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('agrega-cliente/<nombre>/<apellido>/<dni>/<mail>', cliente),
    path('agrega-producto/<bodega>/<etiqueta>/<precio>', producto),
    path('agrega-vendedor/<nombre>/<apellido>/<legajo>', vendedor),
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


]

handler404 = page_not_found_view

    







    # path('listaCursos/', CursoList.as_view() , name= "ListarCursos"),
    # path('detalleCurso/<pk>', CursoDetail.as_view() , name= "DetalleCurso"),
    # path('creaCurso/', CursoCreate.as_view() , name= "CrearCurso"),
    # path('actualizarCurso/<pk>', CursoUpdate.as_view() , name= "ActualizarCurso"),
    # path('eliminarCurso/<pk>', CursoDelete.as_view() , name= "EliminarCurso"),
    # path('registrar', registrar, name= "Registrar"),
    # path('logout', LogoutView.as_view(template_name='logout.html'), name= "Logout"),
    # path('editarPerfil/', editarPerfil, name= "EditarPerfil"),