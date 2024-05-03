from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Transaccion

# Create your views here.
def index(request):
    return HttpResponse("::: Welcome to my site :::")

def list_clientes(request):
    #return HttpResponse("Here you find a list of user")
    clientes = Cliente.objects.all()
    return render(request, 'finance/list_clientes.html', {'clientes': clientes})
def list_transacciones(request):
    #return HttpResponse("Here you find a list of user")
    transacciones = Transaccion.objects.all()
    return render(request, 'finance/list_transacciones.html', {'transacciones': transacciones})
