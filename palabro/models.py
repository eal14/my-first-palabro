from django.db import models

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
