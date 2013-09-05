"""
Este fichero views.py aloja as vistas relacionadas con la aplicacion
como son la pagina home, la de ayuda, la de sobre nosotros y la de contacto
"""
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect

from post.models import *
from users.models import *
from raven.models import *
from django.template import RequestContext
import datetime

def about(request):
    """
    Redirecciona al usuario a la pagina html correpostiente
	al pinchar en la barra de navegacion sobre el boton sobre nosotros.
    """
    return render_to_response('about_us.html', {'title':'Sobre nosotros', 
    'user': request.user},context_instance=RequestContext(request) )

def home(request):
    """
    Redirecciona al usuario a la pagina html correpostiente
	al pinchar en la barra de navegacion sobre el boton home.
    """
    if not request.user.is_authenticated():
        return redirect('/login/?next=%s' % request.path)
    else:
        if request.method == 'POST':
            p = Post.objects.create(
            creator = request.user,
            created = datetime.datetime.now(),
            body = request.POST.get('mensaje'),
            
            )
            p.save()
            return redirect('/home')

        post_ = Post.objects.order_by('created').reverse()
        post = []
        User_ = ExtendUser.objects.all()
        Users = []
        usuario = ExtendUser.objects.get(user = request.user)
        User__ = usuario.followers.all()
        for u in (User_):
            if (u != usuario):
                Users.append(u)
        followers = [] 
        for u in (User__):
            if (u != request.user):
                followers.append(ExtendUser.objects.get(user = u))
       
        for t in post_:
            if t.creator in User__ or t.creator == request.user:
                post.append(t)
        extendido = ExtendUser.objects.get(user = request.user)
           

        return render_to_response('home.html', {'title':'Home', 'Extendido':User_, 'User': request.user, 'post': post, 'Users': Users, 'seguidores': followers, 'Extend': extendido}, context_instance = RequestContext(request))


def help(request):
    """
    Redirecciona al usuario a la pagina html correpostiente
	al pinchar en la barra de navegacion sobre el boton ayuda.
    """
    return render_to_response('help.html', {'title':'Ayuda',
	'user': request.user}, context_instance = RequestContext(request))

def contact(request):
    """
    Redirecciona al usuario a la pagina html correpostiente
	al pinchar en la barra de navegacion sobre el boton contacta.
    """

    if request.method == 'POST':
        subject = request.POST.get('subject', '') 
        message = request.POST.get('message', '')
        from_email = request.POST.get('from_email', '')
        if subject and message and from_email:
            s = sugerencias.objects.create(
                name = subject,
                email = from_email,
                texto = message,
                created = datetime.datetime.now(),    
                )
            s.save()
            return redirect('/contact/')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
    return render_to_response('contact.html', {'title':'Contacto',
    'user': request.user}, context_instance = RequestContext(request) )

def index(request):
    """
    Redirecciona al usuario a la pagina html correpostiente
	al pinchar en la barra de navegacion
    sobre el nombre de nuestra aplicacion RAVEN.
    """
    return render_to_response('index.html', {'title':'Index',
    'user': request.user}, context_instance = RequestContext(request) )

