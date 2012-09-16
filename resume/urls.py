from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from gigs.views import *

urlpatterns = patterns('',
    url(r'^$', SummaryView.as_view(), name='summary'),
    url(r'^work/$', GigListView.as_view(), name='gig-list'),
    url(r'^speaking/$', SpeakingListView.as_view(), name='speaking-list'),
    url(r'^hackathon/$', HackathonListView.as_view(), name='hackathon-list'),
    url(r'^projects/$', ProjectListView.as_view(), name='project-list'),
    url(r'^education/$', EducationView.as_view(), name='education'),
                       
    url(r'^contact/$', ContactView.as_view(), name='contact'),

    # Examples:
    # url(r'^resume/', include('resume.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
