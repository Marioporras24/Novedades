from django.contrib import admin
from ventas.models import *


# Register your models here.
"""
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cod_cliente', 'cupo_credito')
    search_fields = ['cod_empleado']
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Cliente, ClienteAdmin)
"""

admin.site.register(Persona)
admin.site.register(Ciudad)
admin.site.register(Contacto)
admin.site.register(Direccion)
admin.site.register(Empleado)
admin.site.register(CargoEmpleado)
admin.site.register(Eps)
admin.site.register(Arl)
admin.site.register(FondoPension)
admin.site.register(Novedadpersonal)
admin.site.register(Tiponovedadpersonal)