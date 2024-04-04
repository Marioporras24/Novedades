from django import forms
from ventas.models import *
from decimal import Decimal
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.password_validation import validate_password

class AgregarClienteForm(forms.ModelForm):

    documentoidentidad = forms.IntegerField(required=True)
    primer_nombre = forms.CharField(max_length=45)
    segundo_nombre = forms.CharField(max_length=45, required=False)
    primer_apellido = forms.CharField(max_length=45)
    segundo_apellido = forms.CharField(max_length=45, required=False)
    genero = forms.CharField(max_length=20)

    telefono = forms.CharField(max_length=20)
    correo = forms.EmailField(max_length=60)

    direccion = forms.CharField(max_length=60)
    barrio = forms.CharField(max_length=45)
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all())

    class Meta:
        model = Cliente
        fields = ('documentoidentidad', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'genero', 'ciudad', 'barrio',
                   'direccion','telefono', 'correo',  'idtipo_comercio', 'idtipo_cliente', 'cod_cliente', 'cupo_credito')
        labels = {'documentoidentidad':'Documento Identidad', 'primer_nombre':'Primer Nombre','segundo_nombre':'Segundo Nombre', 'primer_apellido':'Primer Apellido',
                  'segundo_apellido':'Segundo Apellido', 'genero':'Genero','telefono':'Telefono', 'correo':'Correo Electronico',
                  'direccion':'Direccion', 'barrio':'Barrio','ciudad':'Ciudad', 'idtipo_comercio':'Tipo de Comercio', 
                  "idtipo_cliente":"Tipo de Cliente", "cod_cliente":"Codigo del Cliente", "cupo_credito":"Cupo de Credito"}
        
class EditarClienteForm(forms.ModelForm):
    
    documentoidentidad = forms.IntegerField(required=True)
    primer_nombre = forms.CharField(max_length=45)
    segundo_nombre = forms.CharField(max_length=45, required=False)
    primer_apellido = forms.CharField(max_length=45)
    segundo_apellido = forms.CharField(max_length=45, required=False)
    genero = forms.CharField(max_length=20)
    telefono = forms.CharField(max_length=20)
    correo = forms.EmailField(max_length=60)
    direccion = forms.CharField(max_length=60)
    barrio = forms.CharField(max_length=45)
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all())
    idtipo_comercio = forms.ModelChoiceField(queryset=TipoComercio.objects.all())
    idtipo_cliente = forms.ModelChoiceField(queryset=TipoCliente.objects.all())

    class Meta:
        model = Cliente
        fields = ('documentoidentidad', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'genero', 'ciudad', 'barrio',
                   'direccion','telefono', 'correo',  'idtipo_comercio', 'idtipo_cliente', 'cod_cliente', 'cupo_credito')
        labels = {
                    'documentoidentidad':'Documento Identidad', 'primer_nombre':'Primer Nombre','segundo_nombre':'Segundo Nombre', 'primer_apellido':'Primer Apellido',
                  'segundo_apellido':'Segundo Apellido', 'genero':'Genero','telefono':'Telefono', 'correo':'Correo Electronico',
                  'direccion':'Direccion', 'barrio':'Barrio','ciudad':'Ciudad', 'idtipo_comercio':'Tipo de Comercio', 
                  "idtipo_cliente":"Tipo de Cliente", "cod_cliente":"Codigo del Cliente", "cupo_credito":"Cupo de Credito"}
        
        widgets = {
            
            'documentoidentidad':forms.TextInput(attrs={'id': 'documentoidentidad_editar'}),
            'primer_nombre':forms.TextInput(attrs={'id':'primernombre_editar'}),
            'segundo_nombre':forms.TextInput(attrs={'id':'segundonombre_editar'}),
            'primer_apellido':forms.TextInput(attrs={'id':'primerapellido_editar'}), 
            'segundo_apellido':forms.TextInput(attrs={'id':'segundoapellido_editar'}),
            'correo':forms.TextInput(attrs={'id':'correo_editar'}),
            'telefono':forms.TextInput(attrs={'id':'telefono_editar'}),
            'direccion':forms.TextInput(attrs={'id':'direccion_editar'}),
            'barrio':forms.TextInput(attrs={'id':'barrio_editar'}),
            'ciudad':forms.TextInput(attrs={'id':'ciudad_editar'}),         
            'genero':forms.TextInput(attrs={'id':'genero_editar'}),   
            'cod_cliente':forms.TextInput(attrs={'type': 'text', 'id': 'codcliente_editar'}),
            'cupo_credito':forms.TextInput(attrs={'id':'cupocredito_editar'}),
            'idtipo_comercio':forms.TextInput(attrs={'id':'tipocomercio_editar'}),
            'idtipo_cliente':forms.TextInput(attrs={'id':'tipocliente_editar'}),
        }

#-----------Empleado -------------


class AgregarEmpleadoForm(forms.ModelForm):
    GENERO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    ]

    RH_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    documentoidentidad = forms.IntegerField(required=True)
    primer_nombre = forms.CharField(max_length=45)
    segundo_nombre = forms.CharField(max_length=45, required=False)
    primer_apellido = forms.CharField(max_length=45)
    segundo_apellido = forms.CharField(max_length=45, required=False)
    genero = forms.ChoiceField(choices=GENERO_CHOICES, widget=forms.Select())
    rh = forms.ChoiceField(choices=RH_CHOICES, widget=forms.Select())

    telefono = forms.CharField(max_length=20)
    correo = forms.EmailField(max_length=60)

    direccion = forms.CharField(max_length=60)
    barrio = forms.CharField(max_length=45)
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all())
    username = forms.CharField(required=True)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Utiliza el widget DateInput
    fecha_ingreso = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Utiliza el widget DateInput
    password = forms.CharField(max_length=60, widget=forms.PasswordInput())
    name = forms.ModelChoiceField(queryset=Group.objects.all(), widget=forms.Select())

    class Meta:
        model = Empleado
        fields = ['documentoidentidad', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'genero', 'ciudad', 'barrio',
                   'direccion','telefono', 'correo','fecha_nacimiento', 'fecha_ingreso', 'salario', 'rh', 'idarl', 'ideps', 'idfondo_pension', 'idcargo_empleado', 'name'] 
        labels = {'documentoidentidad':'Documento Identidad', 'primer_nombre':'Primer Nombre','segundo_nombre':'Segundo Nombre', 'primer_apellido':'Primer Apellido',
                  'segundo_apellido':'Segundo Apellido', 'genero':'Genero','telefono':'Telefono', 'correo':'Correo Electronico',
                  'direccion':'Direccion', 'barrio':'Barrio','ciudad':'Ciudad', 'cod_empleado':'Codigo Empleado', 
                  "fecha_ingresa":"Fecha Ingreso", "salario":"Salario Basico", "fecha_nacimiento":"Fecha Nacimiento", "fecha_ingreso":"Fecha Ingreso", "rh":"RH","idarl":"ARL", "ideps":"EPS", "idfondo_pensoion":"Fondo Pension",
                   "idcargo_empleado":"Cargo Empleado","roles":"Rol Designado"}
        
    

class EditarEmpleadoForm(forms.ModelForm):
    GENERO_CHOICES = [
        ('Seleccionar', 'Seleccionar'),
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    ]

    RH_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    ACTIVO_CHOICES = [
        (True, 'Activo'),
        (False, 'Inactivo'),
    ]


    documentoidentidad = forms.IntegerField(required=True)
    primer_nombre = forms.CharField(max_length=45)
    segundo_nombre = forms.CharField(max_length=45, required=False)
    primer_apellido = forms.CharField(max_length=45)
    segundo_apellido = forms.CharField(max_length=45, required=False)
    genero = forms.ChoiceField(choices=GENERO_CHOICES, widget=forms.Select())
    rh = forms.ChoiceField(choices=RH_CHOICES, widget=forms.Select())
    activo = forms.ChoiceField(choices=ACTIVO_CHOICES, widget=forms.Select())

    telefono = forms.CharField(max_length=20)
    correo = forms.EmailField(max_length=60)

    direccion = forms.CharField(max_length=60)
    barrio = forms.CharField(max_length=45)
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all())
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Utiliza el widget DateInput
    fecha_ingreso = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Utiliza el widget DateInput
    fecha_salida = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) 
    username = forms.CharField(required=True)
    password = forms.CharField(max_length=90, widget=forms.TextInput(attrs={'type': 'password'}))



    class Meta:
        model = Empleado
        exclude = ['cod_empleado', 'idpersona'] 
        fields = ['documentoidentidad', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'genero', 'ciudad', 'barrio',
                   'direccion','telefono', 'correo',  'cod_empleado', 'fecha_nacimiento', 'fecha_ingreso','salario', 'rh', 'idarl', 'ideps', 'idfondo_pension', 'idcargo_empleado', 'iduser', 'roles', 'fecha_salida', 'activo'] 
        labels = {'documentoidentidad':'Documento Identidad', 'primer_nombre':'Primer Nombre','segundo_nombre':'Segundo Nombre', 'primer_apellido':'Primer Apellido',
                  'segundo_apellido':'Segundo Apellido', 'genero':'Genero','telefono':'Telefono', 'correo':'Correo Electronico',
                  'direccion':'Direccion', 'barrio':'Barrio','ciudad':'Ciudad', 'cod_empleado':'Codigo Empleado', 
                  "fecha_ingreso":"Fecha Ingreso", "salario":"Salario Basico", "fecha_nacimiento":"Fecha Nacimiento", "fecha_ingreso":"Fecha Ingreso", "fecha_salida":"fecha Retiro", "rh":"RH","idarl":"ARL", "ideps":"EPS", "idfondo_pensoion":"Fondo Pension",
                   "idcargo_empleado":"Cargo Empleado", "iduser":"Usuario","password":"Contraseña"}
   
    def initializar_campos_relacionados(self, empleado):
        documento = empleado.idpersona
        direccion = documento.iddireccion
        ciudad = direccion.idciudad
        contacto = documento.idcontacto


        self.initial['documentoidentidad'] = documento.documentoidentidad
        self.initial['primer_nombre'] = documento.primer_nombre
        self.initial['segundo_nombre'] = documento.segundo_nombre
        self.initial['primer_apellido'] = documento.primer_apellido
        self.initial['segundo_apellido'] = documento.segundo_apellido
        self.initial['genero'] = documento.genero
        self.initial['ciudad'] = ciudad.idciudad
        self.initial['barrio'] = direccion.barrio
        self.initial['direccion'] = direccion.direccion
        self.initial['telefono'] = contacto.telefono
        self.initial['correo'] = contacto.correo
        self.initial['username'] = empleado.iduser.username       
        self.initial['password'] = empleado.iduser.password
        self.initial['fecha_ingreso'] = empleado.fecha_ingreso.strftime('%Y-%m-%d')
        self.initial['fecha_salida'] = empleado.fecha_salida.strftime('%Y-%m-%d') if empleado.fecha_salida else None
        self.initial['fecha_nacimiento'] = empleado.fecha_nacimiento.strftime('%Y-%m-%d')
        self.initial['activo'] = empleado.activo
        self.initial['roles'] = empleado.roles

    def __init__(self, *args, **kwargs):
        super(EditarEmpleadoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_salida'].required = False        


#------------------- PRODUCTOS-----------------------------
class AgregarProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['cod_producto', 'nombre_producto', 'precio_venta', 'descripcion_producto', 'cantidad_productos', 'imagen', 'idcategoria_producto', 'idtalla'] 
        labels = {'cod_producto':'Codigo Producto', 'nombre_producto':'Producto', 'precio_venta':'Precio', 'descripcion_producto':'Descripcion', 'cantidad_productos':'Cantidad de Productos',
                  'imagen':'Imagen', 'idcategoria_producto':'Categoria Producto', 'idtalla':'Talla Prodcuto'}





#-----------------------INVENTARIOS -----------------------------

class AgregarInventarioForm(forms.ModelForm):

    class Meta:
        model = Inventario
        fields = ['idinventario','fecha_inventario','cantidad_productos', 'cod_producto','idtipo_movimiento','cod_empleado', 'idtalla', 'idubicacion_inventario'] 
        labels = {'idinventario':'Cod Inventario','cantidad_productos':'Cantidad Productos','cod_producto': 'Codigo Producto',
                   'cod_empleado': 'Codigo Empleado', 'idtalla':'Talla','idtipomovimiento_movimiento':'Tipo Movimiento', 'idubicacioninventarioinv':'Ubicacion Producto'}


#------------------- VENTAS -----------------

class AgregarVentaForm(forms.ModelForm):
    total_venta = forms.DecimalField(label='Total Venta', disabled=True, required=False)
    

    class Meta:
        model = Venta
        fields = ['idventa','fecha_venta','cantidad_productos', 'descuento_venta','precio_venta','total_venta','cod_empleado', 'cod_producto', 'cod_cliente'] 
        labels = {'idventa':'No. Venta','fecha_venta':'fecha_venta','cantidad_productos':'Cantidad Productos', 'descuento_venta':'Total Descuento','precio_venta':'Valor Unidad','total_venta':'Total Venta:',
                  'cod_empleado':'Vendido por: ', 'cod_producto':'Producto', 'cod_cliente':'Cliente a Facturar'}
        widgets = {

        }

    def clean(self):
        cleaned_data = super().clean()
        cantidad_productos = int(cleaned_data.get('cantidad_productos'))
        precio_venta = Decimal(cleaned_data.get('cod_producto').precio_venta)
        descuento_venta = Decimal(cleaned_data.get('descuento_venta'))

        if cantidad_productos is not None and precio_venta is not None and descuento_venta is not None:
            total_venta = cantidad_productos * precio_venta - descuento_venta
            cleaned_data['total_venta'] = total_venta

        return cleaned_data
    

    #-----------------------NOVEDAD EMPLEADO -----------------------------

class AgregarNovedadEmpleadoForm(forms.ModelForm):


    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) 
    fechafin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) 
  

    class Meta:
        model = Novedadpersonal
        fields = ['idnovedadpersonal','fecha_inicio','fechafin', 'descripcion','idtiponovedad_personal','codigo_empleado'] 
        labels = {'idnovedadpersonal':'Cod Novedad','fecha_inicio':'Fecha Inicial','fechafin': 'Fecha Final',
                   'cod_empleado': 'Codigo Empleado', 'descripcion':'Descripcion','idtiponovedad_personal':'Tipo Novedad'}


class EditarNovedadEmpleadoForm(forms.ModelForm):
    ESTADO_CHOICES = [
        ('APROBADO', 'APROBADO'),
        ('RECHAZADO', 'RECHAZADO'),
        ('EN REVISION', 'EN REVISION'),
 
    ]

    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})) 
    fechafin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})) 
    estado = forms.ChoiceField(choices=ESTADO_CHOICES, widget=forms.Select())

    class Meta:
        model = Novedadpersonal
        fields = ('idnovedadpersonal', 'fecha_inicio', 'fechafin', 'descripcion', 'idtiponovedad_personal', 'codigo_empleado', 'estado')
        labels = {
            'idnovedadpersonal': 'Cod Novedad',
            'fecha_inicio': 'Fecha Inicial',
            'fechafin': 'Fecha Final',
            'cod_empleado': 'Codigo Empleado',
            'descripcion': 'Descripcion',
            'idtiponovedad_personal': 'Tipo Novedad',
            'estado': 'Estado'
        }
     
    #-----------------------PQRS -----------------------------

class AgregarPqrsForm(forms.ModelForm):

    class Meta:
        model = Pqr
        fields = ['idpqr','fecha_inicio','fecha_cierre', 'motivo_pqr','cod_empleado','cod_cliente', 'idtipopqr', 'idestadopqr'] 
        labels = {'idpqr':'Cod Pqrs','fecha_inicio':'Fecha Inicial','fecha_cierre': 'Fecha Cierre', 'motivo_pqr':'Descripcion',
                   'cod_empleado': 'Codigo Empleado', 'cod_cliente':'Cliente', 'idtipopqr':'Tipo Pqrs', 'idestadopqr':'Estado Actual'}
        exclude = ['fecha_cierre']

    #-----------------------PQRS -----------------------------

class AgregarNovedadProductoForm(forms.ModelForm):


    class Meta:
        model = Novedadproducto
        fields = ['idnovedad_producto','fecha_novedad','descripcion','cantidad_productos','tiponovedad_producto','cod_producto','cod_empleado','idinventario'] 
        labels = {'idnovedadproducto':'Cod Novedad','fecha_novedad':'Fecha Novedad','cantidad_productos':'Cantidad de Prodcutos','tiponovedad_producto':'tipo de Novedad',
                   'cod_empleado': 'Codigo Empleado', 'descripcion':'Descripcion','cod_producto':'Producto','idinventario':'No. Inventario'}

