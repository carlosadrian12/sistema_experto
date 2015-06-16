"""sistema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#`	_*_ coding: utf-8 _*_
from django.conf.urls import include, url
from django.contrib import admin
from sistema.view import principal, declarati, mostrar_declarativos, mostrar_funcional, imperati ,mostrar_orientada, mostrar_struc, mostrar_distri,mostrar_base

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', principal),
    url(r'^index/declarativos.html/$', declarati),
    url(r'^index/declarativos.html/logico.html$',mostrar_declarativos),
    url(r'^index/declarativos.html/base.html$', mostrar_base),
    url(r'^index/declarativos.html/funcional.html$',mostrar_funcional),
    url(r'^index/imperativos.html/$', imperati),
    url(r'^index/imperativos.html/orientada.html$', mostrar_orientada),
    url(r'^index/imperativos.html/estruc.html$', mostrar_struc),
    url(r'^index/imperativos.html/distribuida.html$', mostrar_distri),

 ]
