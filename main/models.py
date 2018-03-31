from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

from django.conf import settings
from django.contrib.postgres.fields import ArrayField

class Room(models.Model):
    booked = models.IntegerField(default=0) 
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False, null = True)

    class Meta:
        ordering = ['timestamp']

class Note(models.Model):
    user = models.TextField(default='')
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    booked = models.BooleanField(default = False)
    room = models.IntegerField(default = 0)
    class Meta:
        ordering = ['timestamp']

            