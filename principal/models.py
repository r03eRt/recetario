#encoding:utf-8 #<- Esta línea permite usar tíldes y caracteres especiales 
from django.db import models #<- Clase con la descripción de modelos
from django.contrib.auth.models import User #<- Llama al modelo usuario
from django.template import RequestContext
from PIL import Image

class Bebida(models.Model):
	nombre = models.CharField(max_length=50)
	ingredientes = models.TextField()
	preparacion = models.TextField()

	def __str__ (self):
    		return self.nombre
    		#cambiar nombre muestra admin return 'Bebida: '+self.nombre


class Receta(models.Model):
	#Dato cadena, longitud máxima 100 y único
	titulo = models.CharField(max_length=100, unique=True)
	#Dato texto, con texto de ayuda
	ingredientes = models.TextField(help_text='Redacta los ingredientes')
	#Dato texto, con nombre: Preparación
	preparacion = models.TextField(verbose_name='Preparación')
	#Dato imagen, se almacenarán en la carpeta recetas, titulo: Imágen
	imagen = models.ImageField(upload_to='photo/', verbose_name='Imagen')
	#Dato Fecha y Hora, almacena la fecha actual
	tiempo_registro = models.DateTimeField(auto_now=True)
	#Enlace al modelo Usuario que Django ya tiene construido
	usuario = models.ForeignKey(User)

	def __str__ (self):
			return self.titulo

class Comentario(models.Model):
	receta=models.ForeignKey(Receta)
	texto= models.TextField(help_text='comentario',verbose_name='comentario')
	
	def __str__ (self):
			return self.texto
		