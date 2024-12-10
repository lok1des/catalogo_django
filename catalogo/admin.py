from django.contrib import admin
from .models import (
    Categoria,
    Marca,
    Proveedor,
    Producto,
    Cliente,
    Venta,
    DetalleVenta,
    Compra,
    DetalleCompra,
    Inventario,
    Promocion,
)


# Personalización del modelo Producto en el panel de administración
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "precio",
        "stock_minimo",
        "categoria",
        "marca",
        "proveedor",
    )
    search_fields = ("nombre",)
    list_filter = ("categoria", "marca", "proveedor")
    ordering = ("nombre",)


# Personalización del modelo Venta en el panel de administración
class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1


class VentaAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "fecha", "total", "usuario")
    search_fields = ("cliente__nombre",)
    list_filter = ("fecha",)
    inlines = [DetalleVentaInline]


# Personalización del modelo Compra en el panel de administración
class DetalleCompraInline(admin.TabularInline):
    model = DetalleCompra
    extra = 1


class CompraAdmin(admin.ModelAdmin):
    list_display = ("id", "proveedor", "fecha", "total", "usuario")
    search_fields = ("proveedor__nombre",)
    list_filter = ("fecha",)
    inlines = [DetalleCompraInline]


# Registro de todos los modelos en el panel de administración
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Proveedor)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Inventario)
admin.site.register(Promocion)
