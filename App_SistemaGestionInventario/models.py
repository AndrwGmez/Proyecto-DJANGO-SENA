from django.contrib.auth.models import AbstractUser
from django.db import models
from .choices import *

# Create your models here.

class CustomUser(AbstractUser):
    id = models.BigAutoField(primary_key = True)
    nombre_1 = models.CharField(max_length=80)
    nombre_2 = models.CharField(max_length=80, blank=True, null=True)
    apellido_1 = models.CharField(max_length=80)
    apellido_2 = models.CharField(max_length=80, blank=True, null=True)
    id_tipo_documento = models.CharField(max_length=11, choices=tipo_documento, default='C.C')
    numero_documento = models.CharField(max_length=80, blank=False, null=False, unique=True)
    correo_sena = models.EmailField(blank=True, null=True, unique=True)
    correo_soy_sena = models.EmailField(blank=False, null=False, unique=True)
    celular_1 = models.CharField(max_length=80, unique=True)
    celular_2 = models.CharField(max_length=80, blank=True, null=True)
    id_rol = models.CharField(max_length=5, choices=rol, default='I.C')
    fecha_inicio_contrato = models.DateField()
    fecha_fin_contrato = models.DateField(blank=True, null=True)
    id_area_instrtuctor = models.CharField(max_length=6, choices=area, default='Soft')
    firma_electronica = models.ImageField()
    permiso_monitor = models.BooleanField(default=False)
    estado_cuenta = models.CharField(max_length=1, choices=estado_cuenta_usuario, default='A')

    def nombre_completo(self):
        return "{} {}".format(self.nombre_1, self.apellido_1)

    def __str__(self):
        return self.nombre_completo()

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )



class Materiales(models.Model):
    id = models.BigAutoField(primary_key = True)
    tipo_material = models.CharField(max_length=7, choices=tipo_material, default='Devo')
    nombre_material = models.CharField(max_length=40)
    modelo_material = models.CharField(max_length=40)
    ubicacion_material = models.CharField(max_length=7, choices=ubicacion_material, default='Z1')
    valor_material = models.IntegerField()
    estado_material = models.CharField(max_length=6, choices=estado_material, default="Dis")
    especificacion_tecnica_material = models.CharField(max_length=150)
    instructor_ecargado_material = models.ForeignKey(CustomUser, related_name='encargado_material', null=False, blank=False, on_delete=models.CASCADE)
    codigo_barras_original_material = models.CharField(max_length=50, blank=False, null=False, unique=True)
    codigo_barras_sena_material = models.CharField(max_length=50, blank=False, null=False, unique=True)
    encargado_registrar_material = models.ForeignKey(CustomUser, related_name='encargado_ingresar_consumible_sistema', null=False, blank=False, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True, default='')
    fecha_ingreso_material = models.DateField(auto_now_add=True)
    actualizacion_material = models.DateField(auto_now_add=True)
    
    class Meta():
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'

    def material_instructor(self):
        return '{} - {} - {}'.format(self.nombre_material, self.codigo_barras_sena_material, self.instructor_ecargado_material)
    
    def __str__(self):
        return self.material_instructor()
    

class Clientes(models.Model):
    id = models.BigAutoField(primary_key=True)
    rol = models.CharField(max_length=5, choices=recibe_material, default='I.P')
    tipo_documento = models.CharField(max_length=11, choices=tipo_documento, default='C.C')
    numero_documento = models.IntegerField(blank=False, null=False, unique=True)
    primer_nombre = models.CharField(max_length=25, blank=False, null=False)
    segundo_nombre = models.CharField(max_length=25, blank=True, null=True)
    primer_apellido = models.CharField(max_length=25, blank=False, null=False)
    segundo_apellido = models.CharField(max_length=25, blank=True, null=True, )
    correo_soy_sena = models.EmailField( blank=False, null=False, default='')
    primer_telefono = models.CharField(max_length=20, blank=False, null=False, unique=True, default='')
    segundo_telefono = models.CharField(max_length=20,blank=True, null=True, default='')
    numero_ficha = models.CharField(max_length=20, blank=True, null=True)
    fecha_ingres_sistema = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def nombre_cliente(self):
        return '{}  {} - {} - {}'.format(self.primer_nombre, self.primer_apellido, self.numero_documento, self.rol,)
    
    def __str__(self):
        return self.nombre_cliente()



class PrestamosConsumibles(models.Model):
    id = models.BigAutoField(primary_key=True)
    encargado_registra_prestamo_consumible = models.ForeignKey(CustomUser, blank=False, null=False, on_delete=models.CASCADE)    
    recibe_prestamo_prestamo_consumible = models.ForeignKey(Clientes, null=False, blank=False, on_delete=models.CASCADE)
    ubicacion_prestamo_prestamo_consumible = models.CharField(max_length=5, choices=ubicacion_material, default='N.A')
    material_otorgado_prestamo_consumible = models.ForeignKey(Materiales, null=False, blank=False, on_delete=models.CASCADE)
    fecha_entrega_prestamo_consumible = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = 'Prestamo consumible'
        verbose_name_plural = 'Prestamos Consumibles'
    
    def formato_prestamo(self):
        return '{} - {}'.format(self.id, self.material_otorgado_prestamo_consumible)

    def __str__(self):
        return self.formato_prestamo()



class PrestamosDevolutivos(models.Model):
    id = models.BigAutoField(primary_key=True)
    encargado_registra_material_devolutivo = models.ForeignKey(CustomUser, blank=False, null=False, on_delete=models.CASCADE)
    recibe_prestamo_material_devolutivo = models.ForeignKey(Clientes, blank=False, null=False, on_delete=models.CASCADE)
    ubicacion_prestamo_material_devolutivo = models.CharField(max_length=5, choices=ubicacion_material, default='Bod')
    material_otorgado_devolutivo = models.ForeignKey(Materiales, null=False, blank=False, on_delete=models.CASCADE)
    estado_prestamo = models.BooleanField(default=True)
    fecha_entrega_material_devolutivo = models.DateField(auto_now_add=True)
    fecha_devolucion_material_devolutivo = models.DateField(blank=False, null=False)

    class Meta():
        verbose_name = 'Prestamo Devolutivo'
        verbose_name_plural = 'Prestamos Devolutivos'

    def formato_prestamo(self):
        return '{} - {}'.format(self.id, self.material_otorgado_devolutivo)
    
    def __str__(self):
        return self.formato_prestamo()
    

