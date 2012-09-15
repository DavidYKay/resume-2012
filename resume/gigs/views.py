from django.http import HttpResponse
from django.views.generic.simple import direct_to_template
from django.template.response import SimpleTemplateResponse
from django.shortcuts import render_to_response

def hello(request):
  return HttpResponse('hello world')

def dashboard(request):
  return direct_to_template(request, 'dashboard.html', locals())
  #return SimpleTemplateResponse('dashboard.html', 
  #                     #context=None,
  #)
