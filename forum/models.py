from django.db import models

class User(models.Model):
    username = models.TextField()
    password = models.TextField()

class Notes(models.Model):
    username = models.TextField()
    note = models.TextField()

#class Messages(models.Model):
 #   username = models.TextField()
  #  message = models.TextField()