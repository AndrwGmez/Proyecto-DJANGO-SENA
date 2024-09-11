tipo_documento = (
    ('C.C', 'Cédula de ciudadanía'),
    ('P.E', 'Permiso especial'),
    ('Pasaporte', 'Pasaporte'),
    ('C.E', 'Cédula de extranjería'),
    ('T.I', 'Tarjeta de identidad'),
    ('R.C', 'Registro civil'),
)

recibe_material = (
    ('I.P', 'Instructor de planta'),
    ('I.C', 'Instructor contratista'),
    ('M', 'Aprendiz'),
    ('ADM', 'Administrativo'),
)


rol = (
    ('I.P', 'Instructor de planta'),
    ('I.C', 'Instructor contratista'),
    ('M', 'Monitor'),
)


estado_cuenta_usuario = (
    ('A', 'Activo'),
    ('I', 'Inactivo')
)

area = (
    ('Soft', 'Software'),
)

tipo_material = (
    ('Consu', 'Consumible'),
    ('Devo', 'Devolutivo'),
)

estado_material = (
    ('Dis', 'Disponible'),
    ('Pres', 'Préstamo'),
    ('Gara', 'Garantía'),
    ('Sop', 'Soporte'),
    ('DB', 'De baja'),
    ('Entr', 'Entregado'),
)

ubicacion_material = (
    ('Bod', 'Bodega'),
    ('Z1', 'Zona 1'),
    ('Z2', 'Zona 2'),
    ('Z3', 'Zona 3'),
    ('Z4', 'Zona 4'),
    ('Z5', 'Zona 5'),
    ('Z6', 'Zona 6'),
    ('Admin', 'Administrativos'),
    ('N.A', 'No aplica'),
    ('Comp', 'Competencia'),
)