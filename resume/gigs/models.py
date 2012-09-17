from django.db import models

from resume.lib.string_utils import nice_date

from embedly import Embedly

class ExternalSite(models.Model):
  name = models.CharField(max_length=50)
  url = models.URLField()
  order = models.IntegerField()

  def __unicode__(self):
    return self.name

  class Meta:
    ordering = ['order', ]

class Platform(models.Model):
  name = models.CharField(max_length=50)
  logo = models.URLField(blank=True)
  appstore_logo = models.URLField(blank=True)

  def __unicode__(self):
    return self.name

class GigType(models.Model):
  name = models.CharField(max_length=50)
  verbose_name = models.CharField(max_length=50)

  def __unicode__(self):
    return self.name

class Gig(models.Model):
  type = models.ForeignKey(GigType)
  name = models.CharField(max_length=50)
  url = models.URLField(blank=True)
  client = models.CharField(blank=True, max_length=50)
  platforms = models.ManyToManyField(Platform, blank=True)
  tagline = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  begin_date = models.DateField()
  end_date = models.DateField(blank=True, null=True)
  logo = models.URLField(blank=True)
  description = models.TextField()

  def formatted_date(self):
    begin_date = nice_date(self.begin_date)
    if self.end_date is None:
      end_date = "Present"
    else:
      end_date = nice_date(self.end_date)

    if begin_date == end_date:
      return begin_date
    else:
      return "%s - %s" % (begin_date, end_date)

  class Meta:
    ordering = ['-end_date', '-begin_date']

  def __unicode__(self):
    return "%s: %s" % (self.client, self.name)

#class SpeakingEvent(models.Model):
#  pass
#
#class Hackathon(models.Model):
#  pass

class Attachment(models.Model):
  gig = models.ForeignKey(Gig)

  class Meta:
    abstract = True

class Video(Attachment):
  url = models.URLField()

  def embed_url(self):
    return "Embed: %s" % (self.url)

  def test_html(self):
    return '3rd world democracy: galaaang Embed: http://www.youtube.com/watch?v=DCL1RpgYxRM'

  def __unicode__(self):
    return "%s: %s" % (self.gig, self.url)

class Photo(Attachment):
  imgur_id = models.CharField(max_length=100)
  title = models.CharField(max_length=50)
  description = models.TextField(blank=True)
  order = models.IntegerField(default=1)
  
  def __unicode__(self):
    return "%s: %s" % (self.title, self.description)

class CodeRepo(Attachment):
  """ Currently this is GitHub only """
  username = models.CharField(max_length=100)
  reponame = models.CharField(max_length=100)
  
  def __unicode__(self):
    return "%s: %s" % (self.username, self.reponame)

class AppStoreListing(Attachment):
  platform = models.ForeignKey(Platform)
  url = models.URLField()
