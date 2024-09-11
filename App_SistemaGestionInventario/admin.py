from django.contrib import admin
from .models import CustomUser, Materiales, Clientes, PrestamosConsumibles, PrestamosDevolutivos

# Register your models here.

#class MaterialesConsumibles_Admin(admin.ModelAdmin):
    #readonly_fields = ('fecha_ingreso_material_consumible', 'actualizacion_material_consumible')

#admin.site.register(MaterialesConsumibles, MaterialesConsumibles_Admin)


#class MaterialesDevolutivos_Admin(admin.ModelAdmin):
    #readonly_fields = ('fecha_ingreso_material_devolutivo', 'actualizacion_material_devolutivo')


#class Prestamos_devolutivos_Admin(admin.ModelAdmin):
    #readonly_fields = ('fecha_prestamo',)

#admin.site.register(Prestamos_devolutivos, Prestamos_devolutivos_Admin)


#class Prestamos_consumible_Admin(admin.ModelAdmin):
    #readonly_fields = ('fecha_prestamo_consumible',)



#admin.site.register(Prestamos_consumible, Prestamos_consumible_Admin)

#admin.site.register(MaterialesDevolutivos, MaterialesDevolutivos_Admin)

admin.site.register(CustomUser)

class Materiales_Admin(admin.ModelAdmin):
    readonly_fields = ('fecha_ingreso_material', 'actualizacion_material')

admin.site.register(Materiales, Materiales_Admin)

admin.site.register(Clientes)
admin.site.register(PrestamosConsumibles)
admin.site.register(PrestamosDevolutivos)