#`	_*_ coding: utf-8 _*_
from django.http import HttpResponse,Http404
from django.template import Template, Context
from django.shortcuts import render, render_to_response
from apps.libreria.models import declarativos , impertativos

def principal(request):
	return render(request,'index.html') 

def declarati(request):
	return render(request,'declarativos.html')

def mostrar_declarativos(request):
	lista_decla= declarativos.objects.filter(tipo='logico')[:10]
	return render_to_response('logico.html',{'lista_decla':lista_decla})

def mostrar_funcional(request):
	lista_decla= declarativos.objects.filter(tipo='Funcional')[:10]
	return render_to_response('funcional.html',{'lista_decla':lista_decla})

def mostrar_base(request):
	lista_decla= declarativos.objects.filter(tipo='base')[:10]
	return render_to_response('base.html',{'lista_decla':lista_decla})

def imperati(request):
	return render(request,'imperativos.html')

def mostrar_orientada(request):
	lista_imper= impertativos.objects.filter(tipo='orientada')[:10]
	return render_to_response('orientada.html',{'lista_imper':lista_imper})

def mostrar_struc(request):
	lista_imper= impertativos.objects.filter(tipo='estructurada')[:10]
	return render_to_response('estruc.html',{'lista_imper':lista_imper})

def mostrar_distri(request):
	lista_imper= impertativos.objects.filter(tipo='distribuida')[:10]
	return render_to_response('distribuida.html',{'lista_imper':lista_imper})
