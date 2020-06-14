# Django imports.
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class Magazine(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

class Article(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	magazine = models.ManyToManyField(Magazine)
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now) 

	class Meta:
		ordering = ['date_posted']

	def __str__(self):
		return self.title