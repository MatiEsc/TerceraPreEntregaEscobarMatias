from django.urls import path, include
from AppTerceraPreEntregaEscobarMatias import views

app_name= "AppTerceraPreEntregaEscobarMatias"

urlpatterns = [
    path('AppTerceraPreEntregaEscobarMatias', views.inicio, name="inicio"),
    path ("cliente/", views.cliente, name="cliente"),
    path("vendedor/", views.vendedor, name= "vendedor"),
    path("proveedor/", views.proveedor, name= "proveedor"),
    path("patrocinante/", views.patrocinante, name= "patrocinante"),
    #path("clienteFormulario", views.clienteFormulario, name="clienteFormulario"),
    #path("vendedorFormulario", views.vendedorFormulario, name="vendedorFormulario"),
    #path("proveedorFormulario", views.proveedorFormulario, name="proveedorFormulario"),
    #path("patrocinanteFormulario", views.patrocinanteFormulario, name="patrocinanteFormulario"),
    path("busquedaCliente", views.busquedaCliente, name="busquedaCliente"),
    path("buscar/", views.buscar),
    path ("leerCliente/", views.leerCliente, name="leerCliente"),
    path ("leerVendedor/", views.leerVendedor, name="leerVendedor"),
    path ("leerProveedor/", views.leerProveedor, name="LeerProveedor"),
    path ("leerPatrocinante/", views.leerPatrocinante, name="LeerleerPatrocinante"),
    path ("eliminarCliente/<cliente_nombre>/", views.eliminarCliente, name="eliminarCliente"),
    path ("editarCliente/<cliente_nombre>/", views.editarCliente, name= "editarCliente"),
    
    ]

