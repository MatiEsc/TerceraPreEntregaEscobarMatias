from django.db import models

# Create your models here.

class Cliente (models.Model):
 
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    email=models.EmailField()
    profesion=models.CharField(max_length=30)

class Vendedor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    email=models.EmailField()

class Proveedor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    email=models.EmailField()
    marca=models.CharField(max_length=30)

class Patrocinante(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    email=models.EmailField()
    marca=models.CharField(max_length=30)


