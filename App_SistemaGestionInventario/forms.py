from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
    input_type = 'date'

class RegistroForm(UserCreationForm):
    fecha_inicio_contrato = forms.DateField(widget=DateInput(attrs={'readonly': 'readonly'}), required=False)
    fecha_fin_contrato = forms.DateField(widget=DateInput(attrs={'readonly': 'readonly'}), required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'nombre_1', 'nombre_2', 'apellido_1', 'apellido_2',
                  'id_tipo_documento', 'numero_documento', 'correo_sena', 'correo_soy_sena',
                  'celular_1', 'celular_2', 'id_rol', 'fecha_inicio_contrato',
                  'fecha_fin_contrato', 'id_area_instrtuctor', 'firma_electronica', 'estado_cuenta']
        widgets = {
            'fecha_inicio_contrato': DateInput(),
            'fecha_fin_contrato': DateInput(),
        }

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nombre_1', 'nombre_2', 'apellido_1', 'apellido_2', 'id_tipo_documento', 'numero_documento', 'correo_sena', 'correo_soy_sena', 'celular_1', 'celular_2', 'fecha_inicio_contrato', 'fecha_fin_contrato', 'firma_electronica']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Deshabilitar las fechas
        self.fields['fecha_inicio_contrato'].disabled = True
        self.fields['fecha_fin_contrato'].disabled = True