"""
ESte fichero forms.py de la parte raven sirve para
crear el formulario de registro de nuestra aplicacion.
"""

from django import forms

class register_user(forms.Form):
    """
    Podemos declarar los campos que son necesarios para el registro de un nuevo usuario en nuestra aplicacion.
    """
    usuario = forms.CharField(max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=10, widget= forms.PasswordInput)
    password2 = forms.CharField(max_length=10, widget= forms.PasswordInput)
