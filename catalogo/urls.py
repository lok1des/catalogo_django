from django.urls import path
from .views import (
    CategoriaListView,
    CategoriaDetailView,
    CategoriaCreateView,
    CategoriaUpdateView,
    CategoriaDeleteView,
)

urlpatterns = [
    # URLs para Categoria
    path("categorias/", CategoriaListView.as_view(), name="categoria-list"),
    path(
        "categorias/<int:pk>/", CategoriaDetailView.as_view(), name="categoria-detail"
    ),
    path("categorias/nueva/", CategoriaCreateView.as_view(), name="categoria-create"),
    path(
        "categorias/<int:pk>/editar/",
        CategoriaUpdateView.as_view(),
        name="categoria-update",
    ),
    path(
        "categorias/<int:pk>/eliminar/",
        CategoriaDeleteView.as_view(),
        name="categoria-delete",
    ),
]
