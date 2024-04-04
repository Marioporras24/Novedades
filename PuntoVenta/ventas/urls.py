from django.urls import path
from . import views





urlpatterns = [

           #-------------- LOGIN --------------------------

    path('', views.iniciar_sesion, name='Inicio'),
    path('Login/', views.iniciar_sesion, name='Login'),
    path('CerrarSesion/', views.cerrar_sesion, name='CerrarSesion'),
    path('empleados/editar/<int:cod_empleado>/', views.editar_Empleado_vista, name='editarEmpleado'),

    

    #----------- CLIENTES----------------
    path('venntas/', views.ventas_vista, name='Ventas'),
    path('clientes/', views.clientes_vista, name='Clientes'),
    path('agregar_Cliente/', views.agregar_Cliente_vista, name='agregarCliente'),
    path('editar_Cliente/', views.editar_Cliente_vista, name='editarCliente'),
    path('eiminar_Cliente/', views.eliminar_Cliente_vista, name='eliminarCliente'),
    #------EMPLEADO ----------
    path('empleados/', views.empleados_vista, name='Empleados'),
    path('agregar_Empleado/', views.agregar_Empleado_vista, name='agregarEmpleado'),
    path('editar_Empleado/<int:cod_empleado>/', views.editar_Empleado_vista, name='editarEmpleado'),
    path('eiminar_Empleado/', views.eliminar_Empleado_vista, name='eliminarEmpleado'),
    path('empleadosInactivos/', views.empleados_inactivos_vista, name='EmpleadosInactivos'),    
    #---------PRODUCTOS--------------
    path('productos/', views.productos_vista, name='Productos'),
    path('agregar_Producto/', views.agregar_Producto_vista, name='agregarProducto'),
   # path('editar_Producto/', views.editar_Producto_vista, name='editarProducto'),
    path('eiminar_Producto/', views.eliminar_Producto_vista, name='eliminarProducto'),
    #-------------- INVENTARIO --------------------------
   path('inventarios/', views.inventarios_vista, name='Inventarios'),
   path('agregar_Inventario/', views.agregar_Inventario_vista, name='agregarInventario'),
   # path('editar_Producto/', views.editar_Inventario_vista, name='editarInventario'),
   path('eiminar_Inventario/', views.eliminar_Inventario_vista, name='eliminarInventario'),
   #---------------- VENTAS ----------------------

   path('agregar_Venta/', views.agregar_Venta_vista, name='agregarVenta'),
   # path('editar_Producto/', views.editar_Inventario_vista, name='editarInventario'),
   path('eiminar_Venta/', views.eliminar_Venta_vista, name='eliminarVenta'),
    #-------------- NOVEDADES PERSONAL --------------------------
   path('novedades_empleados/', views.novedad_Empleado_vista, name='NovedadesEmpleados'),
   path('agregar_Novedad_Empleado/', views.agregar_Novedad_Empleado_vista, name='agregarNovedadEmpleado'),
   path('editar_Novedad_Empleado/<int:idnovedadpersonal>/', views.editar_Novedad_Empleado_vista, name='editarNovedadEmpleado'),
   path('eiminar_NovedadEmpleado/', views.eliminar_Novedad_Empleado_vista, name='eliminarNovedadEmpleado'),

       #-------------- PQRS --------------------------
   path('pqrs/', views.pqrs_vista, name='Pqrs'),
   path('agregar_pqrs/', views.agregar_Pqrs_vista, name='agregarPqrs'),
   # path('editar_Producto/', views.editar_Inventario_vista, name='editarInventario'),
   path('eiminar_pqrs/', views.eliminar_Pqrs_vista, name='eliminarPqrs'),

       #-------------- COTIZACION --------------------------
   path('novedades_Productos/', views.novedad_Producto_vista, name='novedadesProductos'),
   path('agregar_Novedad_Producto/', views.agregar_Novedad_Producto_vista, name='agregarNovedadProducto'),
   # path('editar_Producto/', views.editar_Inventario_vista, name='editarInventario'),
   path('eiminar_Novedad_Producto/', views.eliminar_Novedad_Producto_vista, name='eliminarNovedadProducto'),


]
