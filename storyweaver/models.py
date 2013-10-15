from django.db import models
from django.contrib.auth.models import User

class Narrative(models.Model):
    user = models.ForeignKey(User)
    grid_id = models.CharField(max_length=25)
    title = models.CharField(max_length=100)
    story = models.CharField(max_length=2500)

class Choices(models.Model):
    choice = models.CharField(max_length=2500)
    belongs_to = models.ForeignKey(Narrative)
