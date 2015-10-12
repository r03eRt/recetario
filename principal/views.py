#response
from django.http import HttpResponse

#para imagenes
from django.template import RequestContext

from principal.models import Bebida,Receta,Comentario
from django.shortcuts import render_to_response,get_object_or_404
#queremos usar datos de modelo usuario
from django.contrib.auth.models import User

#definimos vista para recoger lista bebidas
def lista_bebidas(request):
	bebidas = Bebida.objects.all()
	#mandamos todas als variables que queramos a ese 
	return render_to_response('lista_bebidas.html',{'lista_bebidas':bebidas})

#definimos vista para recoger lista recetas
def lista_recetas(request):
	recetas = Receta.objects.all()
	
	return render_to_response('lista_recetas.html',{'lista_recetas':recetas},context_instance=RequestContext(request))


#definimos vista para recoger lista bebidas
def lista_general(request):
	bebidas = Bebida.objects.all()
	recetas = Receta.objects.all()
	comentarios=Comentario.objects.all()
	#mandamos todas als variables que queramos a ese 
	return render_to_response('lista_general.html',{'lista_bebidas':bebidas,'lista_recetas':recetas,'lista_comentarios':comentarios})

#definimos la pantalla de sobre donde devolvemos el textoq ue elegimos
def sobre(request):
	html='<html><body>PROYEFTO DE EJEMPLO </body></html>'
	return HttpResponse(html)


#definimos pantalla de inicio
def inicio(request):
	#recuperamos todos los datos de las recetas
	recetas=Receta.objects.all()
	#le pasamos las recetas a la paginas para mostrarlas,render to response es indicaciond e la plantilla a utilizar
	return render_to_response('inicio.html',{'lista_recetas':recetas})

#vista para mostrar los usuarios registrados y las recetas regiustradas
def usuarios(request):
	usuarios=User.objects.all()
	recetas=Receta.objects.all()
	#le pasamos als variables que vamos a utilizar en las variables
	return render_to_response('usuarios.html',{'lista_usuarios':usuarios,'lista_recetas':recetas})


#defino la vista para el detalle de la receta
def detalle_receta(request,id_receta):
	#moistramos error wsi no la encontramos
	dato=get_object_or_404(Receta,pk=id_receta)
	#filtramos los comentarios de esa receta
	comentarios=Comentario.objects.filter(receta=dato)
	return render_to_response('receta.html',{'receta_filtrada':dato,'lista_comentarios':comentarios},context_instance=RequestContext(request))