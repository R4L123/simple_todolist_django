from django.db import models

class List(models.Model):
  task = models.CharField(max_length=255)
  desc = models.CharField(max_length=255)

  