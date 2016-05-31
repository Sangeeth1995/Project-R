from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Students(models.Model):
	username =models.CharField(max_length=30)
	email=models.EmailField()
	password=models.CharField(max_length=30) 
	def __unicode__(self):
		return self.name

class Projects(models.Model):
	Projectname=models.CharField(max_length=1000)
	Projectyear=models.IntegerField()
	Branch=models.CharField(max_length=30) 
	Projectdescription=models.CharField(max_length=5000) 
	def __unicode__(self):
		return self.Projectname