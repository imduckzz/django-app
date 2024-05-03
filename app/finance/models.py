from django.db import models
from django.contrib.auth.hashers import make_password
import datetime

class DateTimeModel(models.Model):
    created_at =  models.DateTimeField(default=datetime.datetime.now())
    updated_at= models.DateTimeField(default=datetime.datetime.now())
    deleted_at =  models.DateTimeField(null= True, blank= True)  
    class Meta:
        abstract = True

# Create your models here.
class Cliente(DateTimeModel):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(null= True, blank= True)
    password = models.CharField(null= True, blank= True)
    celular = models.CharField(max_length=15, null=True, blank=True)
    def save(self, *args, **kwargs):
        # Encriptar la contraseña antes de guardar
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
class Producto(DateTimeModel):
    nombre_producto = models.CharField(max_length=20)
    abreviatura = models.CharField(max_length=2)
    descripcion = models.TextField()
class Cliente_Producto(DateTimeModel):
    id_cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, blank = False, null=False, default =1)
    id_producto = models.ForeignKey(Producto, on_delete = models.CASCADE, blank = False, null=False, default =1)
    numero_cuenta = models.CharField(max_length=20)
class Tipo_Transaccion(DateTimeModel):
    nombre_transaccion = models.CharField(max_length=20)
    abreviatura = models.CharField(max_length=3)
    descripcion = models.TextField()
class Transaccion(DateTimeModel):
    id_cliente_producto = models.ForeignKey(Cliente_Producto, on_delete = models.CASCADE, blank = False, null=False, default =1)
    monto = models.CharField(max_length=20)
    tipo_transaccion = models.ForeignKey(Tipo_Transaccion, on_delete = models.CASCADE, blank = False, null=False, default =1)

    
    

