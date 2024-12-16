from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
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
from django.shortcuts import render


# Vista para la página de inicio
def inicio(request):
    return render(request, 'inicio.html')


# Vistas para Categoria

# Me muestra una tabla con todas las categorias
class CategoriaListView(ListView):
    model = Categoria
    template_name = "categoria_list.html"
    context_object_name = "categorias"
    # Listo


# Me muestra una página con los detalles de UNA SOLA categoria
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = "categoria_detail.html"
    context_object_name = "categoria"
    # Listo


# Me muestra un formulario para crear una nueva categoria
class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = "categoria_form.html"
    fields = "__all__"
    success_url = reverse_lazy("categoria-list")


# Me muestra un formulario para editar una categoria existente
class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = "categoria_form.html"
    fields = "__all__"
    success_url = reverse_lazy("categoria-list")
    # Listo


# Me muestra un formulario para eliminar una categoria existente
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = "categoria_confirm_delete.html"
    success_url = reverse_lazy("categoria-list")
    # Listo





# Vista de marcas

class MarcaListView(ListView):
    model = Marca
    template_name = 'marcas/marca_list.html'  # Ruta del template
    context_object_name = 'marcas'  # Nombre del contexto a usar en el template

# Crear nueva marca
class MarcaCreateView(CreateView):
    model = Marca
    template_name = 'marcas/marca_form.html'  # Ruta del template
    fields = ['nombre', 'descripcion']  # Campos que aparecerán en el formulario
    success_url = reverse_lazy('marca-list')  # Redirige al listado tras crear

# Detalle de una marca
class MarcaDetailView(DetailView):
    model = Marca
    template_name = 'marcas/marca_detail.html'  # Ruta del template
    context_object_name = 'marca'  # Nombre del contexto a usar en el template

# Actualizar marca
class MarcaUpdateView(UpdateView):
    model = Marca
    template_name = 'marcas/marca_form.html'  # Reutiliza el mismo formulario que para crear
    fields = ['nombre', 'descripcion']  # Campos editables
    success_url = reverse_lazy('marca-list')  # Redirige al listado tras actualizar

# Eliminar marca
class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = 'marcas/marca_confirm_delete.html'  # Ruta del template para confirmar eliminación
    success_url = reverse_lazy('marca-list')  # Redirige al listado tras eliminar
        




#Vista de Proveedores

# Lista de proveedores
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'proveedores/proveedor_list.html'
    context_object_name = 'proveedores'

# Crear un nuevo proveedor
class ProveedorCreateView(CreateView):
    model = Proveedor
    template_name = 'proveedores/proveedor_form.html'
    fields = ['nombre', 'telefono', 'email', 'direccion']
    success_url = reverse_lazy('proveedor-list')

# Detalle de un proveedor
class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = 'proveedores/proveedor_detail.html'
    context_object_name = 'proveedor'

# Actualizar un proveedor existente
class ProveedorUpdateView(UpdateView):
    model = Proveedor
    template_name = 'proveedores/proveedor_form.html'
    fields = ['nombre', 'telefono', 'email', 'direccion']
    success_url = reverse_lazy('proveedor-list')

# Eliminar un proveedor
class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'proveedores/proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedor-list')






#Vista de Productos

# Lista de productos
class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/producto_list.html'
    context_object_name = 'productos'

# Crear un nuevo producto
class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'productos/producto_form.html'
    fields = ['nombre', 'descripcion', 'precio', 'stock_minimo', 'categoria', 'marca', 'proveedor']
    success_url = reverse_lazy('producto-list')

# Detalle de un producto
class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'productos/producto_detail.html'
    context_object_name = 'producto'

# Actualizar un producto existente
class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'productos/producto_form.html'
    fields = ['nombre', 'descripcion', 'precio', 'stock_minimo', 'categoria', 'marca', 'proveedor']
    success_url = reverse_lazy('producto-list')

# Eliminar un producto
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/producto_confirm_delete.html'
    success_url = reverse_lazy('producto-list')







#Urls para Cliente

# Lista de clientes
class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'clientes'

# Crear un nuevo cliente
class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    fields = ['nombre', 'telefono', 'email', 'direccion']
    success_url = reverse_lazy('cliente-list')

# Detalle de un cliente
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'clientes/cliente_detail.html'
    context_object_name = 'cliente'

# Actualizar un cliente existente
class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    fields = ['nombre', 'telefono', 'email', 'direccion']
    success_url = reverse_lazy('cliente-list')

# Eliminar un cliente
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente-list')







#Vista de Ventas

# Lista de ventas
class VentaListView(ListView):
    model = Venta
    template_name = 'ventas/venta_list.html'
    context_object_name = 'ventas'

# Crear una nueva venta
class VentaCreateView(CreateView):
    model = Venta
    template_name = 'ventas/venta_form.html'
    fields = ['cliente', 'total', 'usuario']
    success_url = reverse_lazy('venta-list')

# Detalle de una venta
class VentaDetailView(DetailView):
    model = Venta
    template_name = 'ventas/venta_detail.html'
    context_object_name = 'venta'

# Actualizar una venta existente
class VentaUpdateView(UpdateView):
    model = Venta
    template_name = 'ventas/venta_form.html'
    fields = ['cliente', 'total', 'usuario']
    success_url = reverse_lazy('venta-list')

# Eliminar una venta
class VentaDeleteView(DeleteView):
    model = Venta
    template_name = 'ventas/venta_confirm_delete.html'
    success_url = reverse_lazy('venta-list')






#Vista de Detalle Venta

# Lista de detalles de venta
class DetalleVentaListView(ListView):
    model = DetalleVenta
    template_name = 'detalleventas/detalleventa_list.html'
    context_object_name = 'detalleventas'

# Crear un nuevo detalle de venta
class DetalleVentaCreateView(CreateView):
    model = DetalleVenta
    template_name = 'detalleventas/detalleventa_form.html'
    fields = ['venta', 'producto', 'cantidad', 'precio_unitario', 'subtotal']
    success_url = reverse_lazy('detalleventa-list')

# Detalle de un detalle de venta
class DetalleVentaDetailView(DetailView):
    model = DetalleVenta
    template_name = 'detalleventas/detalleventa_detail.html'
    context_object_name = 'detalleventa'

# Actualizar un detalle de venta
class DetalleVentaUpdateView(UpdateView):
    model = DetalleVenta
    template_name = 'detalleventas/detalleventa_form.html'
    fields = ['venta', 'producto', 'cantidad', 'precio_unitario', 'subtotal']
    success_url = reverse_lazy('detalleventa-list')

# Eliminar un detalle de venta
class DetalleVentaDeleteView(DeleteView):
    model = DetalleVenta
    template_name = 'detalleventas/detalleventa_confirm_delete.html'
    success_url = reverse_lazy('detalleventa-list')





#Vista para Compra

# Lista de compras
class CompraListView(ListView):
    model = Compra
    template_name = 'compras/compra_list.html'
    context_object_name = 'compras'

# Crear nueva compra
class CompraCreateView(CreateView):
    model = Compra
    template_name = 'compras/compra_form.html'
    fields = ['proveedor', 'total', 'usuario']    
    def form_valid(self, form):
        # Si no se selecciona un usuario, asignamos el logueado
        if not form.instance.usuario:
            form.instance.usuario = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('compra-list')

# Detalle de compra
class CompraDetailView(DetailView):
    model = Compra
    template_name = 'compras/compra_detail.html'
    context_object_name = 'compra'

# Editar compra
class CompraUpdateView(UpdateView):
    model = Compra
    template_name = 'compras/compra_form.html'
    fields = ['proveedor', 'total']
    success_url = reverse_lazy('compra-list')

# Eliminar compra
class CompraDeleteView(DeleteView):
    model = Compra
    template_name = 'compras/compra_confirm_delete.html'
    success_url = reverse_lazy('compra-list')








#Views para Detalle Compra

# Vista para la lista de detalles de compra
class DetalleCompraListView(ListView):
    model = DetalleCompra
    template_name = 'detallecompras/detallecompra_list.html'  # Ruta a la carpeta detallecompras
    context_object_name = 'detallecompras'

# Vista para crear un nuevo detalle de compra
class DetalleCompraCreateView(CreateView):
    model = DetalleCompra
    fields = ['compra', 'producto', 'cantidad', 'precio_unitario', 'subtotal']
    template_name = 'detallecompras/detallecompra_form.html'  # Ruta a la carpeta detallecompras
    success_url = reverse_lazy('detallecompra-list')

# Vista para ver los detalles de un detalle de compra
class DetalleCompraDetailView(DetailView):
    model = DetalleCompra
    template_name = 'detallecompras/detallecompra_detail.html'  # Ruta a la carpeta detallecompras
    context_object_name = 'detallecompra'

# Vista para editar un detalle de compra
class DetalleCompraUpdateView(UpdateView):
    model = DetalleCompra
    fields = ['compra', 'producto', 'cantidad', 'precio_unitario', 'subtotal']
    template_name = 'detallecompras/detallecompra_form.html'  # Ruta a la carpeta detallecompras
    success_url = reverse_lazy('detallecompra-list')

# Vista para eliminar un detalle de compra
class DetalleCompraDeleteView(DeleteView):
    model = DetalleCompra
    template_name = 'detallecompras/detallecompra_confirm_delete.html'  # Ruta a la carpeta detallecompras
    success_url = reverse_lazy('detallecompra-list')





#Views para Inventario

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Inventario

# Vista para listar los inventarios
class InventarioListView(ListView):
    model = Inventario
    template_name = 'inventario/inventario_list.html'  
    context_object_name = 'inventarios'

# Vista para ver los detalles de un inventario
class InventarioDetailView(DetailView):
    model = Inventario
    template_name = 'inventario/inventario_detail.html'  
    context_object_name = 'inventario'

# Vista para crear un nuevo inventario
class InventarioCreateView(CreateView):
    model = Inventario
    template_name = 'inventario/inventario_form.html'
    success_url = reverse_lazy('inventario-list')
    fields = ['producto', 'cantidad']  # Especificamos los campos manualmente

# Vista para editar un inventario existente
class InventarioUpdateView(UpdateView):
    model = Inventario
    template_name = 'inventario/inventario_form.html'
    success_url = reverse_lazy('inventario-list')
    fields = ['producto', 'cantidad']  # Especificamos los campos manualmente

# Vista para eliminar un inventario
class InventarioDeleteView(DeleteView):
    model = Inventario
    template_name = 'inventario/inventario_confirm_delete.html'
    success_url = reverse_lazy('inventario-list')





#Views para Promociones
# Vista para listar las promociones
class PromocionListView(ListView):
    model = Promocion
    template_name = 'promocion/promocion_list.html'
    context_object_name = 'promociones'

# Vista para ver los detalles de una promoción
class PromocionDetailView(DetailView):
    model = Promocion
    template_name = 'promocion/promocion_detail.html'
    context_object_name = 'promocion'

# Vista para crear una nueva promoción
class PromocionCreateView(CreateView):
    model = Promocion
    template_name = 'promocion/promocion_form.html'
    success_url = reverse_lazy('promocion-list')
    fields = ['producto', 'descripcion', 'descuento_porcentaje', 'fecha_inicio', 'fecha_fin']

# Vista para editar una promoción existente
class PromocionUpdateView(UpdateView):
    model = Promocion
    template_name = 'promocion/promocion_form.html'
    success_url = reverse_lazy('promocion-list')
    fields = ['producto', 'descripcion', 'descuento_porcentaje', 'fecha_inicio', 'fecha_fin']

# Vista para eliminar una promoción
class PromocionDeleteView(DeleteView):
    model = Promocion
    template_name = 'promocion/promocion_confirm_delete.html'
    success_url = reverse_lazy('promocion-list')