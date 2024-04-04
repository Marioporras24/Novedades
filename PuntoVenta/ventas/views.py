from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from datetime import datetime
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from django.http import HttpResponseForbidden
from django.template.loader import get_template
from django.http import HttpResponse
from django.conf import settings
from django.template import Context








# Create your views here.
"""
def ventas_vista(request):
    num_ventas = 156
    context ={
        'num_ventas': num_ventas
    }
    return render(request, 'ventas.html', context) # aca de coloca el template "el que finaliza en html"
"""



#--------------------------CLIENTES -----------------------

def clientes_vista(request):
    clientes = Cliente.objects.all()
    personas = Persona.objects.all()
    tiposcomercio = TipoComercio.objects.all()
    tiposcliente = TipoCliente.objects.all()
    form_personal = AgregarClienteForm()
    form_editar = EditarClienteForm()
    context ={
        'clientes' : clientes,
        'form_personal' : form_personal,
        'form_editar' : form_editar,

        'personas' : personas,
        'tiposcomercio' : tiposcomercio,
        'tiposcliente': tiposcliente
    }
    return render(request, 'clientes.html', context)

def agregar_Cliente_vista(request):
    if request.method == 'POST':
        form = AgregarClienteForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with transaction.atomic():
                    ciudad = Ciudad.objects.create(
                        ciudad=form.cleaned_data['ciudad'])

                    contacto = Contacto.objects.create(
                        telefono=form.cleaned_data['telefono'],
                        correo=form.cleaned_data['correo']
                        )
                    
                    direccion = Direccion.objects.create(
                        direccion=form.cleaned_data['direccion'],
                        barrio=form.cleaned_data['barrio'],
                        idciudad=ciudad,
                        )

                    persona = Persona.objects.create(
                        documentoidentidad=form.cleaned_data['documentoidentidad'],
                        primer_nombre=form.cleaned_data['primer_nombre'],
                        segundo_nombre=form.cleaned_data['segundo_nombre'],
                        primer_apellido=form.cleaned_data['primer_apellido'],
                        segundo_apellido=form.cleaned_data['segundo_apellido'],
                        genero=form.cleaned_data['genero'],
                        idcontacto=contacto,
                        iddireccion=direccion
                    )

                    cliente = Cliente.objects.create(
                        iddocumento=persona,
                        idtipo_comercio=form.cleaned_data['idtipo_comercio'],
                        idtipo_cliente=form.cleaned_data['idtipo_cliente'],
                        cod_cliente=form.cleaned_data['cod_cliente'],
                        cupo_credito=form.cleaned_data['cupo_credito'],
                    )

                messages.success(request, "Cliente guardado exitosamente")

            except Exception as e:
                messages.error(request, f"Error al cargar la información: {str(e)}")

            return redirect('Clientes')

    return render(request, 'clientes.html', {'form': form})


def editar_Cliente_vista(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditarClienteForm(
            request.POST, request.FILES, instance=cliente)
        if form.is_valid:
            form.save()
    return redirect('Clientes')
        




def eliminar_Cliente_vista(request):
    if request.method == 'POST':
        id_personal_eliminar = request.POST.get('id_personal_eliminar')
        if id_personal_eliminar:
            try:
                cliente = Cliente.objects.get(pk=id_personal_eliminar)
                persona = cliente.iddocumento
                contacto = persona.idcontacto
                direccion = persona.iddireccion

                cliente.delete()
                persona.delete()
                contacto.delete()
                direccion.delete()

                messages.success(request, "Cliente eliminado exitosamente")
            except Cliente.DoesNotExist:
                messages.error(request, "El cliente no existe")
        else:
            messages.error(request, "No se proporcionó un código de cliente válido")
    else:
        return HttpResponseBadRequest("Solicitud no válida")

    return redirect('Clientes')

#---------------------------- EMPLEADOS ---------------
@login_required
@permission_required('ventas.view_empleado', raise_exception=True)
def empleados_vista(request):
    empleados = Empleado.objects.filter(activo=True)
    personas = Persona.objects.all()
    cargoempleado = CargoEmpleado.objects.all()
    eps = Eps.objects.all()
    arl = Arl.objects.all()
    fondopension = FondoPension.objects.all()
    usuario = User.objects.all()
    rolusuario = Group.objects.all()
    form_personal = AgregarEmpleadoForm()
    form_editar = EditarEmpleadoForm()

    username = request.user.username
    context ={
        'empleado' : empleados,
        'form_personal' : form_personal,
        'form_editar' : form_editar,
        'cargoempleado' : cargoempleado,
        'eps' : eps,
        'arl' : arl,
        'fondopension' : fondopension,
        'usuario' : usuario,
        'rolsusuario' : rolusuario,
        'personas' : personas,
        'username': username,

    }
    return render(request, 'empleados.html', context)


@permission_required('ventas.change_empleado', raise_exception=True)
def agregar_Empleado_vista(request):
    if request.method == 'POST':
        form = AgregarEmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with transaction.atomic():
                    ciudad = Ciudad.objects.create(
                        ciudad=form.cleaned_data['ciudad'])


                    contacto = Contacto.objects.create(
                        telefono=form.cleaned_data['telefono'],
                        correo=form.cleaned_data['correo']
                        )
                    
                    direccion = Direccion.objects.create(
                        direccion=form.cleaned_data['direccion'],
                        barrio=form.cleaned_data['barrio'],
                        idciudad=ciudad,
                        )

                    persona = Persona.objects.create(
                        documentoidentidad=form.cleaned_data['documentoidentidad'],
                        primer_nombre=form.cleaned_data['primer_nombre'],
                        segundo_nombre=form.cleaned_data['segundo_nombre'],
                        primer_apellido=form.cleaned_data['primer_apellido'],
                        segundo_apellido=form.cleaned_data['segundo_apellido'],
                        genero=form.cleaned_data['genero'],
                        idcontacto=contacto,
                        iddireccion=direccion
                    )

                    usuario = User.objects.create(
                        username=form.cleaned_data['username']
                    )

                    # Establecer la contraseña de manera segura utilizando set_password
                    usuario.set_password(form.cleaned_data['password'])
                    usuario.save()

                    grupo_nombre = form.cleaned_data['name']
                    grupo = Group.objects.get(name=grupo_nombre)

                    
                    empleado = Empleado.objects.create(
                        idpersona=persona,
                        iduser=usuario,
                        idarl=form.cleaned_data['idarl'],
                        ideps=form.cleaned_data['ideps'],
                        idfondo_pension=form.cleaned_data['idfondo_pension'],
                        idcargo_empleado=form.cleaned_data['idcargo_empleado'],
                        fecha_ingreso=form.cleaned_data['fecha_ingreso'],
                        salario=form.cleaned_data['salario'],
                        fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
                        rh=form.cleaned_data['rh'],
                        roles=grupo,
                    )
                    usuario.groups.add(grupo)

                messages.success(request, "Empleado guardado exitosamente")

            except Exception as e:
                messages.error(request, f"Error al cargar la información: {str(e)}")

            return redirect('Empleados')

    return render(request, 'empleados.html', {'form': form}) 

"""
def editar_Empleado_vista(request, cod_empleado):
    empleado = Empleado.objects.get(cod_empleado=cod_empleado)
    ciudades = Ciudad.objects.all()
    cargos_empleado = CargoEmpleado.objects.all()
    eps = Eps.objects.all()
    arl = Arl.objects.all()
    fondo_pension = FondoPension.objects.all()
    usuario = Usuarioid.objects.all()
    roles_usario = RolUsuario.objects.all()

    if request.method == 'POST':
        # Actualizar los campos del empleado con los datos del formulario
        empleado.fecha_ingreso = datetime.strptime(request.POST.get('fecha_ingreso'), '%Y-%m-%d').date()
        empleado.fecha_nacimiento = datetime.strptime(request.POST.get('fecha_nacimiento'), '%Y-%m-%d').date()

        # Acceder a los atributos del modelo relacionado
        empleado.iddocumento.primer_nombre = request.POST.get('primer_nombre')
        empleado.iddocumento.segundo_nombre = request.POST.get('segundo_nombre')
        empleado.iddocumento.primer_apellido = request.POST.get('primer_apellido')
        empleado.iddocumento.segundo_apellido = request.POST.get('segundo_apellido')

        # Guardar el contacto asociado al empleado
        empleado.iddocumento.idcontacto.telefono = request.POST.get('telefono')
        empleado.iddocumento.idcontacto.correo = request.POST.get('correo')

        # Guardar la dirección asociada al empleado
        empleado.iddocumento.iddireccion.direccion = request.POST.get('direccion')
        empleado.iddocumento.iddireccion.barrio = request.POST.get('barrio')
        empleado.iddocumento.iddireccion.idciudad.ciudad = request.POST.get('ciudad')

        empleado.idcargo_empleado.cargo_empleado = request.POST.get('cargo_empleado')
        empleado.salario = request.POST.get('salario')
        empleado.rh = request.POST.get('rh')
        empleado.ideps.eps = request.POST.get('eps')
        empleado.idarl.arl = request.POST.get('arl')
        empleado.idfondo_pension.fondo_pension = request.POST.get('fondo_pension')
        empleado.idusuario.usuario = request.POST.get('usuario')
        empleado.idusuario.contrasena = request.POST.get('contrasena')
        empleado.idrolusuario.nombre_rol = request.POST.get('nombre_rol')

        # Guardar los cambios
        empleado.save()
        empleado.iddocumento.save() # Guardar el documento relacionado
        empleado.iddocumento.idcontacto.save() # Guardar el contacto relacionado
        empleado.iddocumento.iddireccion.save() # Guardar la dirección relacionada
        empleado.idcargo_empleado.save() # Guardar el cargo del empleado
        empleado.ideps.save() # Guardar la EPS
        empleado.idarl.save() # Guardar la ARL
        empleado.idfondo_pension.save() # Guardar el fondo de pensiones
        empleado.idusuario.save() # Guardar el usuario relacionado
        empleado.idrolusuario.save() # Guardar el rol
        messages.success(request, 'Empleado actualizado correctamente')
        return redirect('Empleados')
    return render(request, 'editarempleado.html', {'empleado':empleado, 'ciudades':ciudades, 'cargos_empleado':cargos_empleado, 'eps':eps,
                                                   'arl':arl, 'fondo_pension':fondo_pension, 'usuario':usuario, 'roles_usuario':roles_usario})
"""
"""

def editar_Empleado_vista(request, cod_empleado):
    empleado = Empleado.objects.get(cod_empleado=cod_empleado)
    ciudades = Ciudad.objects.all()
    cargos_empleado = CargoEmpleado.objects.all()
    eps = Eps.objects.all()
    arl = Arl.objects.all()
    fondo_pension = FondoPension.objects.all()
    usuario = Usuarioid.objects.all()
    roles_usario = RolUsuario.objects.all()    
    form = EditarEmpleadoForm(initial={
        'documentoidentidad': empleado.iddocumento.documentoidentidad,
        'primer_nombre': empleado.iddocumento.primer_nombre,
        'segundo_nombre': empleado.iddocumento.segundo_nombre,
        'primer_apellido': empleado.iddocumento.primer_apellido,
        'segundo_apellido': empleado.iddocumento.segundo_apellido,
        'genero': empleado.iddocumento.genero,
        'telefono': empleado.iddocumento.idcontacto.telefono,
        'correo': empleado.iddocumento.idcontacto.correo,
        'ciudad': empleado.iddocumento.iddireccion.idciudad,
        'direccion': empleado.iddocumento.iddireccion.direccion,
        'barrio': empleado.iddocumento.iddireccion.barrio,
        'cod_empleado': empleado.cod_empleado,
        'fecha_ingreso': empleado.fecha_ingreso,
        'fecha_nacimiento': empleado.fecha_nacimiento,
        'cargo_empleado': empleado.idcargo_empleado,
        'salario': empleado.salario,
        'rh': empleado.rh,
        'eps': empleado.ideps,
        'arl': empleado.idarl,
        'fondo_pension': empleado.idfondo_pension,
        'usuario': empleado.idusuario,
        'contrasena': empleado.idusuario.contrasena,
        'nombre_rol': empleado.idrolusuario,
    })

    return render(request, 'editarempleado.html', {'form': form, 'empleado': empleado, 'ciudades':ciudades, 'cargos_empleado':cargos_empleado, 'eps':eps,
                                                   'arl':arl, 'fondo_pension':fondo_pension, 'usuario':usuario, 'roles_usuario':roles_usario} )
"""
"""
def editar_Empleado_vista(request, cod_empleado):
    empleado = Empleado.objects.get(cod_empleado=cod_empleado)
    
    if request.method == 'POST':
        form_editar = EditarEmpleadoForm(request.POST, instance=empleado)
        if form_editar.is_valid():
            with transaction.atomic():
                # Guarda los datos del formulario en el objeto Empleado
                empleado = form_editar.save(commit=False)
                empleado.save()
                
                # Guarda los datos relacionados
                documento = empleado.iddocumento
                documento.documentoidentidad = form_editar.cleaned_data['documentoidentidad']                
                documento.primer_nombre = form_editar.cleaned_data['primer_nombre']
                documento.segundo_nombre = form_editar.cleaned_data['segundo_nombre']
                documento.primer_apellido = form_editar.cleaned_data['primer_apellido']
                documento.segundo_apellido = form_editar.cleaned_data['segundo_apellido']
                documento.genero = form_editar.cleaned_data['genero']
                documento.save()

                direccion = documento.iddireccion
                direccion.direccion = form_editar.cleaned_data['direccion']
                direccion.barrio = form_editar.cleaned_data['barrio']
                direccion.idciudad = form_editar.cleaned_data['ciudad']
                direccion.save()

                contacto = documento.idcontacto
                contacto.telefono = form_editar.cleaned_data['telefono']
                contacto.correo = form_editar.cleaned_data['correo']
                contacto.save()
                
            return redirect('Empleados')
    else:
        form_editar = EditarEmpleadoForm(instance=empleado)
        form_editar.initializar_campos_relacionados(empleado)
    
    return render(request, 'editarempleado.html', {'form_editar': form_editar, 'empleado': empleado})
"""
"""
def editar_Empleado_vista(request, cod_empleado):
    empleado = Empleado.objects.get(cod_empleado=cod_empleado)
    
    if request.method == 'POST':
        form_editar = EditarEmpleadoForm(request.POST, instance=empleado)
        if form_editar.is_valid():
            with transaction.atomic():
                empleado = form_editar.save(commit=False)
                
                # Guarda los datos de Persona
                persona = empleado.iddocumento
                persona.documentoidentidad = form_editar.cleaned_data['documentoidentidad']
                persona.primer_nombre = form_editar.cleaned_data['primer_nombre']
                persona.segundo_nombre = form_editar.cleaned_data['segundo_nombre']
                persona.primer_apellido = form_editar.cleaned_data['primer_apellido']
                persona.segundo_apellido = form_editar.cleaned_data['segundo_apellido']
                persona.genero = form_editar.cleaned_data['genero']
                persona.save()

                # Actualiza la dirección asociada a la persona
                direccion = persona.iddireccion
                direccion.direccion = form_editar.cleaned_data['direccion']
                direccion.barrio = form_editar.cleaned_data['barrio']
                direccion.idciudad_id = form_editar.cleaned_data['ciudad'].idciudad   # Asigna el ID de la ciudad
                direccion.save()

                # Guarda los demás cambios en el empleado y sus objetos relacionados
                empleado.save()
                empleado.idarl.save()       
                empleado.ideps.save()       
                empleado.idfondo_pension.save()  
                empleado.idcargo_empleado.save()  
                empleado.idusuario.save()   
                empleado.idrolusuario.save()    

            return redirect('Empleados')
    else:
        form_editar = EditarEmpleadoForm(instance=empleado)
        form_editar.initializar_campos_relacionados(empleado)
    
    return render(request, 'editarempleado.html', {'form_editar': form_editar, 'empleado': empleado})
"""


@login_required

def editar_Empleado_vista(request, cod_empleado):
    empleado = Empleado.objects.get(cod_empleado=cod_empleado)
    
    if request.method == 'POST':
        form_editar = EditarEmpleadoForm(request.POST, instance=empleado)
        if form_editar.is_valid():
            with transaction.atomic():
                # Guarda los datos del formulario en el objeto Empleado
                empleado = form_editar.save(commit=False)
                empleado.save()
                # Guarda los objetos relacionados
                
                # Guarda los datos de Persona
                persona = empleado.idpersona
                persona.documentoidentidad = form_editar.cleaned_data['documentoidentidad']                
                persona.primer_nombre = form_editar.cleaned_data['primer_nombre']
                persona.segundo_nombre = form_editar.cleaned_data['segundo_nombre']
                persona.primer_apellido = form_editar.cleaned_data['primer_apellido']
                persona.segundo_apellido = form_editar.cleaned_data['segundo_apellido']
                persona.genero = form_editar.cleaned_data['genero']
                persona.save()

                direccion = empleado.idpersona.iddireccion
                direccion.direccion = form_editar.cleaned_data['direccion']
                direccion.barrio = form_editar.cleaned_data['barrio']
                direccion.idciudad = form_editar.cleaned_data['ciudad']  # Cambia a idciudad
                direccion.save()
                
                if empleado.iduser:
                    usuario = empleado.iduser
                else:
                    usuario = User()
                usuario.username = form_editar.cleaned_data['username']
                if form_editar.cleaned_data['password']:
                    usuario.set_password(form_editar.cleaned_data['password'])
                usuario.save()
                

                contacto = empleado.idpersona.idcontacto
                contacto.telefono = form_editar.cleaned_data['telefono']
                contacto.correo = form_editar.cleaned_data['correo']
                contacto.save()
                # Actualiza el rol del usuario asociado al empleado
                usuario = empleado.iduser
                grupo_nombre = form_editar.cleaned_data['roles']
                grupo = Group.objects.get(name=grupo_nombre)
                usuario.groups.clear()  # Elimina los roles existentes
                usuario.groups.add(grupo)                 
                
            return redirect('Empleados')
    else:
        form_editar = EditarEmpleadoForm(instance=empleado)
        form_editar.initializar_campos_relacionados(empleado)
    
    return render(request, 'editarempleado.html', {'form_editar': form_editar, 'empleado': empleado})


"""
    documento_documento = empleado.iddocumento.documentoidentidad
    documento_primer_nombre = empleado.iddocumento.primer_nombre
    documento_segundo_nombre = empleado.iddocumento.segundo_nombre
    documento_primer_apellido = empleado.iddocumento.primer_apellido
    documento_segundo_apellido = empleado.iddocumento.segundo_apellido
    documento_genero = empleado.iddocumento.genero   
    documento_ciudad = empleado.iddocumento.iddireccion.idciudad   
    documento_barrio = empleado.iddocumento.iddireccion.barrio
    documento_direccion = empleado.iddocumento.iddireccion.direccion   
    documento_telefono = empleado.iddocumento.idcontacto.telefono  
    documento_correo = empleado.iddocumento.idcontacto.correo   
    contrasena = empleado.idusuario.contrasena 
    fecha_ingreso = empleado.fecha_ingreso.strftime('%Y-%m-%d') 
    fecha_nacimiento = empleado.fecha_nacimiento.strftime('%Y-%m-%d') 
         
    form_editar.fields['documentoidentidad'].initial = documento_documento
    form_editar.fields['primer_nombre'].initial = documento_primer_nombre
    form_editar.fields['segundo_nombre'].initial = documento_segundo_nombre
    form_editar.fields['primer_apellido'].initial = documento_primer_apellido
    form_editar.fields['segundo_apellido'].initial = documento_segundo_apellido    
    form_editar.fields['genero'].initial = documento_genero
    form_editar.fields['ciudad'].initial = documento_ciudad    
    form_editar.fields['barrio'].initial = documento_barrio
    form_editar.fields['direccion'].initial = documento_direccion                    
    form_editar.fields['telefono'].initial = documento_telefono
    form_editar.fields['correo'].initial = documento_correo
    form_editar.fields['contrasena'].initial = contrasena
    form_editar.fields['fecha_ingreso'].initial = fecha_ingreso
    form_editar.fields['fecha_nacimiento'].initial = fecha_nacimiento   
"""    

@login_required
@permission_required('ventas.delete_empleado', raise_exception=True)
def eliminar_Empleado_vista(request):
    if request.method == 'POST':
        id_personal_eliminar = request.POST.get('id_personal_eliminar')
        if id_personal_eliminar:
            try:
                empleado = Empleado.objects.get(pk=id_personal_eliminar)
                usuario = empleado.iduser
                persona = empleado.idpersona
                contacto = persona.idcontacto
                direccion = persona.iddireccion

                usuario.delete() 
                persona.delete()
                contacto.delete()
                direccion.delete()
                empleado.delete()

                messages.success(request, "Cliente eliminado exitosamente")
            except Cliente.DoesNotExist:
                messages.error(request, "El cliente no existe")
        else:
            messages.error(request, "No se proporcionó un código de cliente válido")
    else:
        return HttpResponseBadRequest("Solicitud no válida")

    return redirect('Empleados')

def permission_denied_view(request, exception):
    return render(request, 'miapp/error_permiso.html', status=403)




#------------- PRODUCTOS -------------------
@login_required
def productos_vista(request):
    producto = Producto.objects.all()
    talla = Talla.objects.all()
    categoriaproducto = CategoriaProducto.objects.all()
    form_personal = AgregarProductoForm()
   # form_editar = EditarEmpleadoForm()
    context ={
        'producto' : producto,
        'form_personal' : form_personal,
  #      'form_editar' : form_editar,
        'talla' : talla,
        'categoriaproducto' : categoriaproducto,
    }

    return render(request, 'productos.html', context)

def agregar_Producto_vista(request):
    if request.method == 'POST':
        form = AgregarProductoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request,"error al guardar el producto")
                return redirect('Productos')

    return redirect('Productos')

"""

def editar_Producto_vista(request):
    cliente = get_object_or_404(Cliente, pk="id_personal_editar")
    if request.method == 'POST':
        form = EditarProductoForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            # Redireccionar o realizar alguna acción después de guardar los cambios
    else:
        form = EditarProdcutoForm(instance=cliente)
    return redirect('Productos')
"""
@login_required
def eliminar_Producto_vista(request):
    if request.method == 'POST':
        id_personal_eliminar = request.POST.get('id_personal_eliminar')
        if id_personal_eliminar:
            try:
                producto = Producto.objects.get(pk=id_personal_eliminar)

                producto.delete() 

            except Producto.DoesNotExist:
                messages.error(request, "El Producto no existe")

    return redirect('Productos')


#-------------------- Inventario 
@login_required
def inventarios_vista(request):
    inventario = Inventario.objects.all()
    empleado = Empleado.objects.all()
    producto = Producto.objects.all()
    tipomovimiento = Tipomovimiento
    talla = Talla.objects.all()
    ubicacion = Ubicacioninventario.objects.all()
    form_personal = AgregarInventarioForm()
   # form_editar = EditarEmpleadoForm()
    context ={
        'inventario' : inventario,
        'empleado' : empleado,
        'tipomovimiento' : tipomovimiento,
        'producto' : producto,
        'ubicacion' : ubicacion,
        'form_personal' : form_personal,
  #      'form_editar' : form_editar,
        'talla' : talla,
    }

    return render(request, 'inventarios.html', context)

@login_required
def agregar_Inventario_vista(request):
    if request.method == 'POST':
        form = AgregarInventarioForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Guardar la entrada de inventario
                inventario = form.save()

                # Obtener el producto correspondiente al código del producto ingresado en el formulario
                codigo_producto = inventario.cod_producto.cod_producto
                producto = Producto.objects.get(cod_producto=codigo_producto)

                # Sumar la cantidad de productos del inventario al total de productos del modelo Producto
                producto.cantidad_productos += inventario.cantidad_productos
                producto.save()

                # Redireccionar a la página de inventarios
                return redirect('Inventarios')

            except Exception as e:
                # Manejar el error si ocurre algún problema
                messages.error(request, f"Error al guardar el Inventario: {str(e)}")
    else:
        form = AgregarInventarioForm()

    return redirect('Inventarios')

@login_required
def eliminar_Inventario_vista(request):
    if request.method == 'POST':
        id_personal_eliminar = request.POST.get('id_personal_eliminar')
        if id_personal_eliminar:
            try:
                inventario = Inventario.objects.get(pk=id_personal_eliminar)

                inventario.delete() 

            except Inventario.DoesNotExist:
                messages.error(request, "El inventario no existe")

    return redirect('Inventarios')



#-------------------- VENTAS-------------------
@login_required
def ventas_vista(request):

    venta = Venta.objects.all()
    empleado = Empleado.objects.all()
    producto = Producto.objects.all()
    cliente = Cliente.objects.all()
    form_personal = AgregarVentaForm()
   # form_editar = EditarEmpleadoForm()
    context ={
        'venta' : venta,
        'empleado' : empleado,
        'cliente' : cliente,
        'producto' : producto,
        'form_personal' : form_personal,
  #      'form_editar' : form_editar,
    }

    return render(request, 'ventas.html', context)
@login_required
def agregar_Venta_vista(request):
    if request.method == 'POST':
        form = AgregarVentaForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request,"error al guardar el producto")
                return redirect('Ventas')

    return redirect('Ventas')

@login_required
def eliminar_Venta_vista(request):
    if request.method == 'POST':
        id_personal_eliminar = request.POST.get('id_personal_eliminar')
        if id_personal_eliminar:
            try:
                venta = Venta.objects.get(pk=id_personal_eliminar)

                venta.delete() 

            except Venta.DoesNotExist:
                messages.error(request, "No es posible")

    return redirect('Ventas')

# --------------NOVEDADES PERSONAL -----------------
@login_required
@permission_required('ventas.view_novedadpersonal', raise_exception=True)
def novedad_Empleado_vista(request):
    novedadpersonal = Novedadpersonal.objects.all()
    tiponovedad = Tiponovedadpersonal.objects.all()
    empleado = Empleado.objects.all()
    form_personal = AgregarNovedadEmpleadoForm()
    form_editar = EditarNovedadEmpleadoForm()
    context ={
        'novedadpersonal' : novedadpersonal,
        'tiponovedad' : tiponovedad,
        'form_editar' : form_editar,
        'empleado' : empleado,
        'form_personal' : form_personal,
    }

    return render(request, 'novedadesempleados.html', context)

@login_required
@permission_required('ventas.add_novedadpersonal', raise_exception=True)
def agregar_Novedad_Empleado_vista(request):
    if request.method == 'POST':
        form = AgregarNovedadEmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request,"error al guardar el Novedad")
                return redirect('NovedadesEmpleados')

    return redirect('NovedadesEmpleados')

@login_required
@permission_required('ventas.change_novedadpersonal', raise_exception=True)
def editar_Novedad_Empleado_vista(request, idnovedadpersonal):
    # Obtenemos la instancia de la Novedadpersonal
    novedadpersonal = get_object_or_404(Novedadpersonal, idnovedadpersonal=idnovedadpersonal)

    if novedadpersonal.estado in ["APROBADO", "RECHAZADO"]:
        messages.error(request, "Esta novedad ya ha sido procesada y no se puede modificar.")
        return redirect('NovedadesEmpleados')
    
    if request.method == 'POST':
        form_editar = EditarNovedadEmpleadoForm(request.POST, instance=novedadpersonal)
        if form_editar.is_valid():
            form_editar.save()
            
            # Obtenemos el correo electrónico del empleado asociado a la novedad de empleado
            correo_empleado = novedadpersonal.codigo_empleado.idpersona.idcontacto.correo
            tipo_novedad = novedadpersonal.idtiponovedad_personal.novedad_personal


            # Llamamos a la función enviar_correo con el estado de la novedad y el correo del empleado
            enviar_correo(novedadpersonal.estado, correo_empleado, idnovedadpersonal, tipo_novedad)


            return redirect('NovedadesEmpleados')
    else:
        form_editar = EditarNovedadEmpleadoForm(instance=novedadpersonal)
    
    return render(request, 'editarnovedad.html', {'form_editar': form_editar, 'novedadpersonal': novedadpersonal})


def enviar_correo(estado, correo_empleado, idnovedadpersonal, tipo_novedad):
    # Define el mensaje de correo basado en el estado de la novedad
    if estado == "APROBADO":
        subject = 'Respuesta Novedades Empleados'
        message = ("Buen dia!\n\n" 
                   f"Su solicitud de {tipo_novedad} No. {idnovedadpersonal} ha sido APROBADA.\n\n"
                    "Cordialmente,\n"
                    "Siud-Updenim.")
        
    elif estado == "RECHAZADO":
        subject = 'Respuesta Novedades Empleados'
        message = ("Buen dia!\n\n" 
                   f"Su solicitud de {tipo_novedad}  No. {idnovedadpersonal} ha sido RECHAZADA.\n\n"
                    "Cordialmente,\n"
                    "Siud-Updenim.")

    else:
        # Manejar un estado desconocido o inválido si es necesario
        subject = 'Novedad de empleado'
        message = f'su Solicitud de {tipo_novedad} No. {idnovedadpersonal} ha cambiado de estado.'

    # Envía el correo electrónico
    send_mail(
        subject,
        message,
        'updenim.notificaciones@gmail.com',
        [correo_empleado],
        fail_silently=False,
    )

@login_required
@permission_required('ventas.delete_novedadpersonal', raise_exception=True)
def eliminar_Novedad_Empleado_vista(request):
    if request.method == 'POST':
        id_personal_eliminar = request.POST.get('id_personal_eliminar')
        if id_personal_eliminar:
            try:
                novedadpersonal = Novedadpersonal.objects.get(pk=id_personal_eliminar)

                novedadpersonal.delete() 

            except Novedadpersonal.DoesNotExist:
                messages.error(request, "La Novedad no existe")

    return redirect('NovedadesEmpleados')


# --------------PQRS -----------------
@login_required
def pqrs_vista(request):
    pqrs = Pqr.objects.all()
    tipopqrs = TipoPQR.objects.all()
    estadopqrs = EstadoPQR.objects.all()
    empleado = Empleado.objects.all()
    cliente = Cliente.objects.all()
    form_personal = AgregarPqrsForm()
   # form_editar = EditarEmpleadoForm()
    context ={
        'pqrs' : pqrs,
        'tipopqrs' : tipopqrs,
  #      'form_editar' : form_editar,
         'empleado' : empleado,
         'estadopqrs': estadopqrs,
         'cliente' : cliente,
        'form_personal' : form_personal,
    }

    return render(request, 'pqrs.html', context)
@login_required
def agregar_Pqrs_vista(request):
    if request.method == 'POST':
        form = AgregarPqrsForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request,"error al registrar PQRS")
                return redirect('Pqrs')

    return redirect('Pqrs')

@login_required
def eliminar_Pqrs_vista(request):
    if request.method == 'POST':
        id_personal_eliminar = request.POST.get('id_personal_eliminar')
        if id_personal_eliminar:
            try:
                pqrs = Pqr.objects.get(pk=id_personal_eliminar)

                pqrs.delete() 

            except Pqr.DoesNotExist:
                messages.error(request, "La PQRS no existe")

    return redirect('Pqrs')


# --------------NOVEDADES PRODUCTOS -----------------
@login_required
def novedad_Producto_vista(request):
    novedadproducto = Novedadproducto.objects.all()
    tiponovedad = Tiponovedadproducto.objects.all()
    inventario = Inventario.objects.all()
    estadopqrs = EstadoPQR.objects.all()
    empleado = Empleado.objects.all()
    cliente = Cliente.objects.all()
    form_personal = AgregarNovedadProductoForm()
   # form_editar = EditarEmpleadoForm()
    context ={
        'novedadproducto' : novedadproducto,
        'tiponovedad' : tiponovedad,
  #      'form_editar' : form_editar,
         'empleado' : empleado,
         'estadopqrs': estadopqrs,
         'cliente' : cliente,
         'inventario' : inventario,
        'form_personal' : form_personal,
    }

    return render(request, 'novedadesproductos.html', context)

@login_required
def agregar_Novedad_Producto_vista(request):
    if request.method == 'POST':
        form = AgregarNovedadProductoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request,"error al registrar Novedad")
                return redirect('novedadesProductos')

    return redirect('novedadesProductos')

@login_required
def eliminar_Novedad_Producto_vista(request):
    if request.method == 'POST':
        id_personal_eliminar = request.POST.get('id_personal_eliminar')
        if id_personal_eliminar:
            try:
                novedadproducto = Novedadproducto.objects.get(pk=id_personal_eliminar)

                novedadproducto.delete() 

            except Novedadproducto.DoesNotExist:
                messages.error(request, "La PQRS no existe")

    return redirect('novedadesProductos')


#------------- LOGIN -----------------

def iniciar_sesion(request):
    # Verifica si la solicitud es un POST (es decir, si se envió un formulario de inicio de sesión)
    if request.method == "POST":
        # Crea una instancia del formulario de autenticación y pasa los datos de la solicitud POST
        form = AuthenticationForm(request, data=request.POST)
        
        # Verifica si los datos del formulario son válidos
        if form.is_valid():
            # Obtiene el nombre de usuario y la contraseña del formulario
            nombre_usuario = form.cleaned_data.get("username")
            contrasena = form.cleaned_data.get("password")
            
            # Autentica al usuario utilizando el nombre de usuario y la contraseña
            usuario = authenticate(username=nombre_usuario, password=contrasena)
            
            # Verifica si la autenticación fue exitosa (es decir, si se encontró un usuario con las credenciales proporcionadas)
            if usuario is not None:
                # Inicia sesión para el usuario en la solicitud actual
                login(request, usuario)
                
                # Redirige a la página de empleados después de iniciar sesión exitosamente
                return redirect('Empleados')
            else:
                # Si la autenticación falla, muestra un mensaje de error
                messages.error(request, 'Usuario o contraseña no válidos')
        else:
            # Si los datos del formulario no son válidos, muestra un mensaje de error
            messages.error(request, 'Datos inválidos')
    else:
        # Si la solicitud no es un POST, crea una instancia del formulario de autenticación vacío
        form = AuthenticationForm()
    
    # Renderiza la plantilla de inicio de sesión (login.html) y pasa el formulario como contexto
    return render(request, "login.html", {"form": form})


def cerrar_sesion(request):
    logout(request)

    return redirect('Login')




@login_required
@permission_required('ventas.view_empleado', raise_exception=True)
def empleados_inactivos_vista(request):
    empleados = Empleado.objects.filter(activo=False)
    personas = Persona.objects.all()
    cargoempleado = CargoEmpleado.objects.all()
    eps = Eps.objects.all()
    arl = Arl.objects.all()
    fondopension = FondoPension.objects.all()
    usuario = Usuarioid.objects.all()
    rolusuario = RolUsuario.objects.all()
    form_personal = AgregarEmpleadoForm()
    form_editar = EditarEmpleadoForm()

    username = request.user.username
    context ={
        'empleado' : empleados,
        'form_personal' : form_personal,
        'form_editar' : form_editar,
        'cargoempleado' : cargoempleado,
        'eps' : eps,
        'arl' : arl,
        'fondopension' : fondopension,
        'usuario' : usuario,
        'rolsusuario' : rolusuario,
        'personas' : personas,
        'username': username,

    }
    return render(request, 'empleadosinactivos.html', context)