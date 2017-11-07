from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Language(models.Model):
	description = models.CharField(max_length=50)
	short_description = models.CharField(max_length=10, blank=True, null=True)
	
	def __str__(self):
	    return '%s' % (self.description)

class WordType(models.Model):
	description = models.CharField(max_length=50)
	short_description = models.CharField(max_length=10, blank=True, null=True)

class RelationType(models.Model):
	description = models.CharField(max_length=50)
	short_description = models.CharField(max_length=10, blank=True, null=True)
	
class Genre(models.Model):
    identifier = models.CharField(max_length=1)
    description = models.CharField(max_length=50)
    short_description = models.CharField(max_length=10, blank=True, null=True)

# This is the main table, here I will agregate all objects i know,
# in my original language (spanish) (cause it needs a description to know what object i refer..)
# **Correction: It can be in any language.. 'cause not all languages have same things..
# and they can be intercaled.
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
    city = models.CharField(max_length=100, null=True)
    country_code = models.CharField(max_length=3, null=True)
    country_code3 = models.CharField(max_length=3, null=True)
    latitude = models.CharField(max_length=25, null=True)
    longitude = models.CharField(max_length=25, null=True)
    counter = models.IntegerField()

class Visit(models.Model):
    visitor = models.ForeignKey(Visitor)
    visit_date = models.DateTimeField(default=timezone.now)
    visited_page = models.CharField(max_length=40)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    native_language = models.ForeignKey(Language, null=True)
    birthdate = models.DateTimeField(null=True)
    genre = models.ForeignKey(Genre, null=True)
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
