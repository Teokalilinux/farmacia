from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    # Define los campos que se mostrarán en la lista de productos
    list_display = ('nombre', 'droga', 'stock', 'precio', 'fecha')
    
    # Define los campos en los que se puede buscar
    search_fields = ('nombre', 'droga', 'precio')
    
    # Define los campos por los que se puede filtrar
    list_filter = ('droga',)

# Registra el modelo con su configuración personalizada
admin.site.register(Producto, ProductoAdmin)
