# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# This is our model for user registration.
class user_registration(models.Model):

	### followings are the fields of our table.
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	mobile = models.CharField(max_length=12)
	password = models.CharField(max_length=50)
	address = models.CharField(max_length=200)

	### It will help to print the values.
	def __str__(self):
		return '%s %s %s %s %s %s' % (self.fname, self.lname, self.email, self.mobile, self.password, self.address)