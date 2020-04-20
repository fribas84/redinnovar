from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


motivo= ['Participar imprimiendo','Contacto', 'Donacion de materiales'  ]

class Contacto(forms.Form):
    Nombre = forms.CharField(label='Nombre', max_length=100, required= True)
    Email = forms.EmailField(label='Email', required=True)
    
    Asunto = forms.CharField(label='Asunto', max_length=100, required=True)
    Mensaje = forms.CharField(label = 'Mensaje', widget=forms.Textarea, max_length=500, required=True)
    
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
           'Nombre',
           'Email',
           'Asunto',
           'Mensaje',
            Submit('submit', 'Enviar')
        )

