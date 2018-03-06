from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

from django.conf import settings
from django.contrib.postgres.fields import ArrayField

class Room(models.Model):
    user = ArrayField(models.IntegerField(default=0))
    booked = models.IntegerField(default=0) 
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    change_date = ArrayField(models.TextField(null = True))
    end_date = models.DateField(blank=True, null = True)

    class Meta:
        ordering = ['timestamp']

    