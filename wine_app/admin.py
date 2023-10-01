from django.contrib import admin
from .models import Vendedores, Productos, Clientes

admin.site.site_header = "Panel administración WineApp"

class WineAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido')
    search_fields = ('nombre', 'apellido')
    list_filter = ('nombre','apellido')


class WineAdmin2(admin.ModelAdmin):
    list_display = ('bodega','etiqueta')
    search_fields = ('bodega','etiqueta')
    list_filter = ('bodega','etiqueta')

# Register your models here.

admin.site.register(Vendedores, WineAdmin)
admin.site.register(Productos, WineAdmin2)
admin.site.register(Clientes, WineAdmin)

