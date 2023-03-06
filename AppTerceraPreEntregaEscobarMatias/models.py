from django.db import models

# Create your models here.

class Clientes (models.Model):
 
    nombre=models.CharField(max_length=40)
    dni=models.IntegerField()
    email=models.EmailField()
    profesion=models.CharField(max_length=30)

class Vendedores(models.Model):
    nombre=models.CharField(max_length=40)
    dni=models.IntegerField()
    email=models.EmailField()

class Proveedores(models.Model):
    nombre=models.CharField(max_length=40)
    dni=models.IntegerField()
    email=models.EmailField()
    marca=models.CharField(max_length=30)

class Patrocinantes(models.Model):
    nombre=models.CharField(max_length=40)
    dni=models.IntegerField()
    email=models.EmailField()
    marca=models.CharField(max_length=30)


