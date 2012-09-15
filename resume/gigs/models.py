from django.db import models

# Create your models here.

class Gig(models.Model):
  name = models.CharField(max_length=50)
  client = models.CharField(max_length=50)
  location = models.DateTimeField()
  begin_date = models.DateTimeField()
  end_date = models.DateTimeField()
  logo = models.URLField()
  description = models.TextField()

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

class Photo(Attachment):
  title = models.CharField(max_length=50)
  description = models.TextField()
  order = models.IntegerField()

class CodeRepo(Attachment):
  url = models.URLField()
