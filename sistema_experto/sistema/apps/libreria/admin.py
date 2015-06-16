#`	_*_ coding: utf-8 _*_
from django.contrib import admin
from apps.libreria.models import impertativos,declarativos
# Register your models here.


# Register your models here.
class imper(admin.ModelAdmin):
	list_display =('nombre','tipo',)
	list_filter = ('nombre',)
	field = ('nombre','tipo')
	pass

class decla(admin.ModelAdmin):
	list_display =('nombre','tipo',)
	list_filter = ('nombre',)
	#date_hierarchy='fecha_publicacion'
	field = ('nombre','tipo')
	'''#filter_horizontal = ('nombre')'''
	# o filter vertical = (autores)
	#cuando se tiene muchas opciones es recomendable usar cuadros de busquedas
	#raw_id_fields = (editor)

admin.site.register(impertativos,imper)
admin.site.register(declarativos,decla)
