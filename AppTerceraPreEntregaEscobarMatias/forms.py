from django import forms


class ClienteFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    dni=forms.IntegerField()
    email=forms.EmailField()
    profesion=forms.CharField(max_length=30)

class VendedorFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    dni=forms.IntegerField()
    email=forms.EmailField()

class ProveedorFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    dni=forms.IntegerField()
    email=forms.EmailField()
    marca=forms.CharField(max_length=30)

class PatrocinanteFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    dni=forms.IntegerField()
    email=forms.EmailField()
    marca=forms.CharField(max_length=30)
