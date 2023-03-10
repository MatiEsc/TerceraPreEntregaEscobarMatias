from django.shortcuts import render
from django.http import HttpResponse
from AppTerceraPreEntregaEscobarMatias.models import Cliente, Vendedor, Proveedor, Patrocinante
from AppTerceraPreEntregaEscobarMatias.forms import ClienteFormulario, VendedorFormulario, ProveedorFormulario, PatrocinanteFormulario

# Create your views here.
"""
def cliente(self):
    cliente= Cliente (nombre="Matias", apellido="Escobar" dni=12123123, email="matias@coder.it")
    cliente.save()

    documentoDeTexto= f"--- nombre:{cliente.nombre} apellido: {cliente.apellido} dni: {cliente.dni} email: {cliente.email}"
    return HttpResponse (documentoDeTexto)
"""

def inicio (request):
    return render (request, "inicio.html")


def cliente(request):
    if request.method =="POST":
        miFormulario= ClienteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion=miFormulario.cleaned_data

        cliente= Cliente (nombre=informacion ["nombre"],
                          apellido=informacion ["apellido"],
                          dni=informacion ["dni"],
                          email=informacion ["email"],
                          profesion=informacion ["profesion"],)
            
        cliente.save()

        return render(request, "inicio.html")
    else:
        miFormulario= ClienteFormulario()

    return render(request, "cliente.html", {"miFormulario":miFormulario})


def vendedor(request):
    if request.method =="POST":
        miFormulario= VendedorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion=miFormulario.cleaned_data

        vendedor= Vendedor (nombre=informacion ["nombre"],
                          apellido=informacion ["apellido"],
                          dni=informacion ["dni"],
                          email=informacion ["email"],)
            
        vendedor.save()

        return render(request, "inicio.html")
    else:
        miFormulario= VendedorFormulario()

    return render(request, "vendedor.html", {"miFormulario":miFormulario})

def proveedor(request):
    if request.method =="POST":
        miFormulario= ProveedorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion=miFormulario.cleaned_data

        proveedor= Proveedor (nombre=informacion ["nombre"],
                          apellido=informacion ["apellido"],
                          dni=informacion ["dni"],
                          email=informacion ["email"],
                          marca=informacion ["marca"],)
            
        proveedor.save()

        return render(request, "inicio.html")
    else:
        miFormulario= ProveedorFormulario()

    return render(request, "proveedor.html", {"miFormulario":miFormulario})

def patrocinante(request):
    if request.method =="POST":
        miFormulario= PatrocinanteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion=miFormulario.cleaned_data

        patrocinante= Patrocinante(nombre=informacion ["nombre"],
                          apellido=informacion ["apellido"],
                          dni=informacion ["dni"],
                          email=informacion ["email"],
                          marca=informacion ["marca"],)
            
        patrocinante.save()

        return render(request, "inicio.html")
    else:
        miFormulario= PatrocinanteFormulario()

    return render(request, "patrocinante.html", {"miFormulario":miFormulario})


def busquedaCliente (request):
    return render (request, "busquedaCliente.html")

def buscar (request):
   if request.GET["dni"]:
       dni= request.GET["dni"]
       cliente= Cliente.objects.filter(dni__icontains=dni)

       return render(request, "resultadoBusqueda.html", {"cliente":cliente, "dni":dni})
   
   else:
       respuesta= "No enviaste datos."
   
   return HttpResponse(respuesta)

def leerCliente(request):
    cliente= Cliente.objects.all()
    contexto = {"cliente": cliente}
    return render (request, "leerCliente.html", contexto)

def leerVendedor(request):
    vendedor= Vendedor.objects.all()
    contexto = {"vendedor": vendedor}
    return render (request, "leerVendedor.html", contexto)

def leerProveedor(request):
    proveedor= Proveedor.objects.all()
    contexto = {"proveedor": proveedor}
    return render (request, "leerProveedor.html", contexto)

def leerPatrocinante(request):
    patrocinante= Patrocinante.objects.all()
    contexto = {"patrocinante": patrocinante}
    return render (request, "leerPatrocinante.html", contexto)

def eliminarCliente(request, cliente_nombre):
    cliente= Cliente.objects.get(nombre=cliente_nombre)
    cliente.delete()

    cliente=Cliente.objects.all()
    contexto = {"cliente": cliente}
    return render (request, "leerCliente.html", contexto)

def editarCliente(request, cliente_nombre):
    cliente= Cliente.objects.get(nombre=cliente_nombre)

    if request.method == "POST":
        miFormulario= ClienteFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid(): 
            informacion= miFormulario.cleaned_data

            cliente.nombre= informacion ["nombre"]
            cliente.apellido= informacion ["apellido"]
            cliente.dni= informacion ["dni"]
            cliente.email= informacion ["email"]
            cliente.profesion= informacion ["profesion"]

            cliente.save()

            return render(request, "inicio.html")
        
    else:
        miFormulario= ClienteFormulario(initial={"nombre": cliente.nombre, 
                                                     "apellido":cliente.apellido, 
                                                     "dni":cliente.dni, 
                                                     "email":cliente.email, 
                                                     "profesion": cliente.profesion})
            
        return render (request, "editarCliente.html",
                            {"miFormulario":miFormulario, "cliente_nombre":cliente_nombre})



