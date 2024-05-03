from django.contrib import admin
from.models import Cliente, Producto,Cliente_Producto,Tipo_Transaccion,Transaccion

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Cliente_Producto)
admin.site.register(Tipo_Transaccion)
admin.site.register(Transaccion)
