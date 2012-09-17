from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
#def active(request, pattern):
def active(request, url_name):
  import re
  #import pdb; pdb.set_trace()
  #print "Request was: %s, pattern was: %s" % (request, pattern)
  #if request != '' and re.search(pattern, request.path):
  pattern = "^%s$" % reverse(url_name)
  if pattern != '' and re.search(pattern, request.path):
    #print "MATCH FOUND pattern was: %s" % (pattern)
    return 'active'
  else:
    pass
    #print "NO MATCH FOUND pattern was: %s" % (pattern)
  return ''
