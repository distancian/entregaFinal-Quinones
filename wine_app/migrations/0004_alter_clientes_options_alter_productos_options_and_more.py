# Generated by Django 4.2.4 on 2023-10-01 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine_app', '0003_rename_categoria_productos_bodega_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientes',
            options={'ordering': ('nombre', 'apellido', 'dni', 'mail'), 'verbose_name': 'Cliente', 'verbose_name_plural': 'clientes'},
        ),
        migrations.AlterModelOptions(
            name='productos',
            options={'ordering': ('bodega',), 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelOptions(
            name='vendedores',
            options={'ordering': ('nombre',), 'verbose_name': 'Vendedor', 'verbose_name_plural': 'Vendedores'},
        ),
        migrations.AddField(
            model_name='productos',
            name='detalle',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='clientes',
            unique_together={('nombre', 'dni')},
        ),
        migrations.AlterUniqueTogether(
            name='productos',
            unique_together={('bodega', 'etiqueta')},
        ),
        migrations.AlterUniqueTogether(
            name='vendedores',
            unique_together={('legajo',)},
        ),
    ]