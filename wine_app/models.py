from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    mail = models.EmailField()

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'
    
    class Meta():
        verbose_name = 'Cliente'
        verbose_name_plural = 'clientes'
        ordering = ('nombre', 'apellido', 'dni', 'mail')
        unique_together = ('nombre', 'dni')

class Vendedores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    legajo = models.IntegerField()  

    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.legajo}' 
    
    class Meta():
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'    
        ordering = ('nombre',)
        unique_together = ('legajo',)
        

class Productos(models.Model):
    bodega = models.CharField(max_length=40)
    etiqueta = models.CharField(max_length=40)
    precio = models.IntegerField()

    def __str__(self):
        return f'{self.bodega} - {self.etiqueta}'

    class Meta():
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'  
        ordering = ('bodega',)
        unique_together = ('bodega', 'etiqueta')
