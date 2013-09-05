"""
Fichero models.py recoge el modelo de datos para los post
que quieran realizar nuestros usuarios ya sean
post propios o respuestas a post de nuestros amigos.
"""
from django.db import models
from users.models import User
from django.contrib import admin

class Reply(models.Model):
    """
    Aqui se endican los datos necesarios
    para realizar una respuesta a un post.
    """
    body = models.TextField(max_length=155)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)


class Post(models.Model):
    """
    Aqui se endican los datos necesarios
    para publicar un post.
    """
    body = models.TextField(max_length=155)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)
    reply = models.ManyToManyField(Reply)
    


##ADMIN


class PostAdmin(admin.ModelAdmin):
    """
    Como se almacenan los post.
    """
    list_display = ["creator", "created"]
    list_filter = ["creator"]

class ReplyAdmin(admin.ModelAdmin):
    """
    Como se almacenan las respuestas.
    """
    list_display = ["creator", "created"]
    list_filter = ["creator"]

admin.site.register(Post, PostAdmin)
admin.site.register(Reply, ReplyAdmin)
