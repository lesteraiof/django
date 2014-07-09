#from django.shortcuts import render
from django.http import HttpResponse
from demo.apps.ventas.models import producto
from django.core import serializers

# Create your views here.

def wsProductos_view(request):
	#Retorna en formato JSON
	data=serializers.serialize("json",producto.objects.filter(status=True))	
	return HttpResponse(data,mimetype='application/json') 
	
	#Retorna en formato XML
	#data=serializers.serialize("xml",producto.objects.filter(status=True))	
	#return HttpResponse(data,mimetype='application/xml') 	