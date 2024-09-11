from django.urls import path, include
from App_SistemaGestionInventario import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import RegistroUsuario


urlpatterns = [
    path('', views.home, name="index_principal"),
    path('funciones_ingreso/', views.funciones_ingreso_rol, name='funciones_ingreso_rol'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir/',views.salir_sistema, name="salir"),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='App_SistemaGestionInventario/general/formulario.html'), name="password_reset"),
    path('reset_password_send/',auth_views.PasswordResetDoneView.as_view(template_name='App_SistemaGestionInventario/general/confirmacion_done.html'), name="password_reset_done"),
    path('reset_/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_completo/',auth_views.PasswordResetCompleteView.as_view(template_name='App_SistemaGestionInventario/general/contrasena_cambiada_exitosamente.html'), name="password_reset_complete"),


    #Permiso monitor    
    path('vista-permisos-monitor/', views.vista_permisos_monitor, name='vista_permisos_monitor'),    
    path('accion-permisos-todos/', views.accion_permisos_todos, name='accion_permisos_todos'),
    path('error-acceso-denegado/', views.error_acceso_denegado_monitor, name='error_acceso_denegado'),   
   

    #Plantillas generales
    
    path('index_info/', views.index_info, name="index_info"),



    #Plantillas administrador
    path('fun_admin/', views.funciones_administrador, name="funciones_administrador"),
    path('calen_admin/', views.calendario_administrador, name="calendario_administrador"),
    path('crear_usu/', RegistroUsuario.as_view(), name="crear_usuario"),
    path('reg_mate_admin/', views.registrar_materiales_administrador, name="registrar_materiales_administrador"),
    path('ver_usu/', views.visualizar_usuarios, name="visualizar_usuarios"),
    path('gene_repor_admin/', views.generar_reporte_admin, name="generar_reporte_admin"),
    path('dar_permi_admin/', views.vista_permisos_administrador, name="vista_permisos_administrador"),
    path('lis_mate_consu_admin/', views.listar_materiales_consumibles_administrador, name="listar_materiales_consumibles_administrador"),
    path('cuenta_admin/', views.visualizar_cuenta_administrador, name="visualizar_cuenta_administrador"),
    path('entre_consu_admin/', views.entregable_consumible_administrador, name="entregable_consumible_administrador"),
    path('entre_devo_admin/', views.entregable_devolutivo_administrador, name="entregable_devolutivo_administrador"),
    path('lis_mate_sup_admin/', views.listar_material_soporte_administrador, name="listar_material_soporte_administrador"),
    path('lis_mate_devo_admin/', views.listar_materiales_devolutivos_administrador, name="listar_materiales_devolutivos_administrador"),
    path('lis_mate_garan_admin/', views.listar_material_garantia_administrador, name="listar_material_garantia_administrador"),
    path('lis_mate_baja_admin/', views.listar_material_baja_administrador, name="listar_material_baja_administrador"),
    path('edi_mate_devo_admin/', views.editar_material_devolutivo_admininistrador, name="editar_material_devolutivo_admininistrador"),
    path('edi_mate_consu_admin/', views.editar_materiales_consumibles_administrador, name="editar_materiales_consumibles_administrador"),
    path('reto_devo_admin/', views.retornar_devolutivo_administrador, name="retornar_devolutivo_administrador"),
 

    #Plantillas instructor de planta
    path('fun_ins_planta/', views.funciones_instructor_planta, name="funciones_instructor_planta"),
    path('lis_usu_planta', views.lista_usuarios_planta, name="lista_usuarios"),
    path('regis_mate_ins_planta/', views.registrar_material_instructor_planta, name="registrar_material_instructor_planta"),
    path('lis_mate_consu_planta/', views.listar_materiales_consumibles_planta, name="listar_materiales_consumibles_planta"),
    path('lis_mate_devo_planta/', views.listar_materiales_devolutivos_planta, name="listar_materiales_devolutivos_planta"),
    path('calen_planta/', views.calendario_planta, name="calendario_planta"),
    path('dar_permi_planta/', views.vista_permisos_monitor_planta, name="vista_permisos_monitor_planta"),
    path('lis_mate_garan_planta/', views.listar_material_garantia_planta, name="listar_material_garantia_planta"),
    path('lis_mate_baja_planta/', views.listar_material_baja_planta, name="listar_material_baja_planta"),
    path('lis_mate_sopor_planta/', views.listar_material_soporte_planta, name="listar_material_soporte_planta"),
    path('entre_consu_planta/', views.entregable_consumible_planta, name="entregable_consumible_planta"),
    path('entre_devo_planta/', views.entregable_devolutivo_planta, name="entregable_devolutivo_planta"),
    path('ver_cuenta_planta/', views.visualizar_cuenta_planta, name="visualizar_cuenta_planta"),
    path('generar_reportes/', views.generar_reporte, name="generar_reporte"),
    path('generar-reporte-pdf/', views.generar_reporte_pdf_materiales, name='generar_reporte_pdf'),
    path('generar_excel/', views.generar_excel_materiales, name='generar_excel'),
    path('generar_excel_prestamo/', views.generar_excel_prestamo, name='generar_excel_prestamo'),
    path('generar_excel_consumible/', views.generar_excel_consumible, name='generar_excel_consumible'),
    path('generar_excel_clientes/', views.generar_excel_clientes, name='generar_excel_clientes'),
    path('generar_excel_usuario/', views.generar_excel_usuario, name='generar_excel_usuario'),
    path('reto_devo_planta/', views.retornar_devolutivo_planta, name="retornar_devolutivo_planta"),
    path('edi_mate_devo_planta/', views.editar_material_devolutivo_planta, name="editar_material_devolutivo_planta"),
    path('edi_mate_consu_planta/', views.editar_materiales_consumibles_planta, name="editar_materiales_consumibles_planta"),


    #Plantillas instructor de contrato
    path('fun_ins_contra/', views.funciones_instructor_contrato, name="funciones_instructor_contrato"),
    path('lis_usu_contra', views.listar_usuarios_contrato, name="lista_usuarios_contra"),
    path('regis_mate_ins_contra/', views.registrar_materiales_instructor_contrato, name="registrar_materiales_instructor_contrato"),
    path('calen_contra/', views.calendario_contrato, name="calendario_contrato"),
    path('lis_mate_baja_contra/', views.listar_material_baja_contrato, name="listar_material_baja_contrato"),
    path('lis_mate_consu_contra/', views.listar_material_consumible_contrato, name="listar_material_consumible_contrato"),
    path('lis_mate_devo_contra/', views.listar_material_devolutivo_contrato, name="listar_material_devolutivo_contrato"),
    path('lis_mate_garan_contra/', views.listar_material_garantia_contrato ,name="listar_material_garantia_contrato"),
    path('lis_mate_sup_contra/', views.listar_material_soporte_contrato, name="listar_material_soporte_contrato"),
    path('entre_consu_contra/', views.entregable_consumible_contrato, name="entregable_consumible_contrato"),
    path('entre_devo_contra/', views.entregable_devolutivo_contrato, name="entregable_devolutivo_contrato"),
    path('ver_cuenta_contra/', views.visualizar_cuenta_contra, name="visualizar_cuenta_contra"),
    path('reto_devo_contrato/', views.retornar_devolutivo_contrato, name="retornar_devolutivo_contrato"),
    path('edi_mate_consu_contra/', views.editar_materiales_consumibles_contratista, name="editar_materiales_consumibles_contratista"),
    path('edi_mate_devo_contra/', views.editar_materiales_devolutivos_contratista, name="editar_materiales_devolutivos_contratista"),

    #Plantillas monitor
    path('fun_moni/', views.funciones_monitor, name="funciones_monitor"),
    path('lis_mate_devo_moni/', views.listar_material_devolutivo_monitor, name="listar_material_devolutivo_monitor"),
    path('lis_mate_consu_moni/', views.listar_material_consumible_monitor, name="listar_material_consumible_monitor"), 
    path('calen_moni/', views.calendario_monitor, name="calendario_monitor"),
    path('regis_mate_moni/', views.registrar_material_monitor, name="registrar_material_monitor"),
    path('ver_cuenta_monitor/', views.visualizar_cuenta_monitor, name="visualizar_cuenta_monitor"),
    path('entre_consu_monitor/', views.entregable_consumible_monitor, name="entregable_consumible_monitor"),
    path('entre_devo_monitor/', views.entregable_devolutivo_monitor, name="entregable_devolutivo_monitor"),
    path('reto_devo_monitor/', views.retornar_material_devolutivo_monitor, name="retornar_material_devolutivo_monitor")

]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)