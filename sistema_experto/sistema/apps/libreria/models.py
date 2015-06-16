#`	_*_ coding: utf-8 _*_
from django.db import models

# Create your models here.
class impertativos(models.Model):
	nombre=models.CharField(max_length = 30)
	tipo=models.CharField(max_length=50)
	
	class Meta:
		ordering = ['nombre']
		#verbose_name_plural = "Editores"
		pass

	def __unicode__(self):
		return self.nombre
		pass
	pass

class declarativos(models.Model):
	nombre = models.CharField(max_length = 30)
	tipo   = models.CharField(max_length = 30)
	
	class Meta:
		ordering = ['nombre']
		#verbose_name_plural = "Editores"
		pass

	def __unicode__(self):
		return self.nombre
		pass
	pass
	