from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.response import SimpleTemplateResponse
from django.utils import timezone
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.simple import direct_to_template

from models import Gig, GigType, ExternalSite

def hello(request):
  return HttpResponse('hello world')

class SummaryView(TemplateView):
  template_name = "summary.html"
  
  def get_context_data(self, **kwargs):
    context = super(SummaryView, self).get_context_data(**kwargs)
    context['page_title'] = 'Summary'
    context['external_sites'] = ExternalSite.objects.all()
    return context

class GigListView(ListView):
  queryset = Gig.objects.filter(type=GigType.objects.get(name='contract'))

  def get_context_data(self, **kwargs):
    context = super(GigListView, self).get_context_data(**kwargs)
    context['now'] = timezone.now()
    context['page_title'] = 'Work'
    return context

class SpeakingListView(ListView):
  queryset = Gig.objects.filter(type=GigType.objects.get(name='speaking'))

  def get_context_data(self, **kwargs):
    context = super(SpeakingListView, self).get_context_data(**kwargs)
    context['page_title'] = 'Speaking'
    return context

class HackathonListView(ListView):
  queryset = Gig.objects.filter(type=GigType.objects.get(name='hackathon'))
  
  def get_context_data(self, **kwargs):
    context = super(HackathonListView, self).get_context_data(**kwargs)
    context['page_title'] = 'Hackathons'
    return context

class ProjectListView(ListView):
  queryset = Gig.objects.filter(type=GigType.objects.get(name='project'))
  
  def get_context_data(self, **kwargs):
    context = super(ProjectListView, self).get_context_data(**kwargs)
    context['page_title'] = 'Projects'
    return context

class EducationView(TemplateView):
  template_name = "education.html"
  
  def get_context_data(self, **kwargs):
    context = super(EducationView, self).get_context_data(**kwargs)
    context['page_title'] = 'Education'
    return context

class ContactView(TemplateView):
  template_name = "contact.html"
  
  def get_context_data(self, **kwargs):
    context = super(ContactView, self).get_context_data(**kwargs)
    context['page_title'] = 'Contact'
    return context
