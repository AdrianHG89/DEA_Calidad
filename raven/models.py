"""
ESte fichero models.py de la parte raven recoge el
modelo del formalario de contacto que se almacena
en la base de dato es solo accesible por el admin.
"""
from django.db import models
from django.contrib import admin
class sugerencias(models.Model):
    """
	Muestra los campos que debera rellenar un usuario
	que se quiera poner en contacto con el admin de la web
    """
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    texto = models.CharField(max_length=600)
    created = models.DateTimeField(auto_now_add=True)

class sugerenciasAdmin(admin.ModelAdmin):
    """
    No se le muestra al admin los mensajes
    """
    list_display = ["email"]
    list_filter = ["created"]


admin.site.register(sugerencias, sugerenciasAdmin)


