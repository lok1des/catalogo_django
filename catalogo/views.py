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
