from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("list_clientes",views.list_clientes, name='list_cliente'),
    path("list_transacciones",views.list_transacciones, name='list_transaccion'),
]
