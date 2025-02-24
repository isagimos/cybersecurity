from django.db import models

class User(models.Model):
    username = models.TextField()
    password = models.TextField()

class PersonalNotes(models.Model):
    username = models.TextField()
    note = models.TextField()