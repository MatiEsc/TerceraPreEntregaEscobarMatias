from django.db import models

# Create your models here.

class Cliente (models.Model):
 
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    email=models.EmailField()
    profesion=models.CharField(max_length=30)

    def __str__(self):
        return f"nombre:{self.nombre} - apellido:{self.apellido} - dni:{self.dni} - email: {self.email} - profesion: {self.profesion}"

class Vendedor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return f"nombre:{self.nombre} - apellido:{self.apellido} - dni:{self.dni} - email: {self.email}"

class Proveedor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    email=models.EmailField()
    marca=models.CharField(max_length=30)

    def __str__(self):
        return f"nombre:{self.nombre} - apellido:{self.apellido} - dni:{self.dni} - email: {self.email} - marca: {self.marca}"

class Patrocinante(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    email=models.EmailField()
    marca=models.CharField(max_length=30)


    def __str__(self):
        return f"nombre:{self.nombre} - apellido:{self.apellido} - dni:{self.dni} - email: {self.email} - marca: {self.marca}"

