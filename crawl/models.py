from __future__ import unicode_literals

from django.db import models

# Create your models here.

class search_tag(models.Model):
	tag = models.CharField(max_length=20)

	def __unicode__(self):
		return unicode(self.tag)