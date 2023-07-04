from django.db import models

class DataUser(models.Model):
    Nombre = models.TextField(max_length=8)
    Apellidos = models.TextField(max_length=16)
    Gmail = models.TextField(max_length=24)
    Descripcion = models.TextField(max_length=50)
    Usuario = models.TextField(max_length=8)
    Contraseña = models.TextField(max_length=12)
    Imagen = models.ImageField(upload_to='user_images/')