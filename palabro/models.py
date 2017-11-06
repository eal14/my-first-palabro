from django.db import models
from django.utils import timezone

# Create your models here.

class Language(models.Model):
	description = models.CharField(max_length=50)
	short_description = models.CharField(max_length=10, blank=True, null=True)

class WordType(models.Model):
	description = models.CharField(max_length=50)
	short_description = models.CharField(max_length=10, blank=True, null=True)

class RelationType(models.Model):
	description = models.CharField(max_length=50)
	short_description = models.CharField(max_length=10, blank=True, null=True)

# This is the main table, here I will agregate all objects i know,
# in my original language (spanish) (cause it needs a description to know what object i refer..)
class Thing(models.Model):
	description = models.CharField(max_length=100)
	abreviation = models.CharField(max_length=20, blank=True, null=True)

class Phrase(models.Model):
	description = models.CharField(max_length=1000)
	abreviation = models.CharField(max_length=20, blank=True, null=True)
	language = models.ForeignKey(Language)

class Visitor(models.Model):
    ip = models.CharField(max_length=128, primary_key=True)
    created_dtim = models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length=100)
    country_code = models.CharField(max_length=3)
    country_code3 = models.CharField(max_length=3)
    latitude = models.CharField(max_length=25)
    longitude = models.CharField(max_length=25)
    counter = models.IntegerField()

class Visit(models.Model):
    visitor = models.ForeignKey(Visitor)
    visit_date = models.DateTimeField(default=timezone.now)
    visited_page = models.CharField(max_length=40)

#class user
    
