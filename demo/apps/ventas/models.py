from django.db import models

# Create your models here.

class cliente(models.Model):
		nombre=models.CharField(max_length=200)
		apellidos=models.CharField(max_length=200)
		status=models.BooleanField(default=True)

		def __unicode__(self):
			nombrecompleto="%s %s"%(self.nombre,self.apellidos)
			return nombrecompleto

class producto(models.Model):	

		def url(self,filename):
			ruta="MultimediaData/Productos/%s/%s"%(self.nombre,str(filename))
			return ruta

		nombre=models.CharField(max_length=100)
		descripcion=models.TextField(max_length=300)
		status=models.BooleanField(default=True)		
		imagen=models.ImageField(upload_to=url,null=True,blank=True)		
		precio=models.DecimalField(max_digits=6,decimal_places=2)
		stock=models.IntegerField()		

		def __unicode__(self):			
			return self.nombre

