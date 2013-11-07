import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

GENDER = (
    ("Male", 'Male'),
    ("Female", 'Female'),
    ("Other", 'Other'),
    ("None", 'None'),
)

class Narrative(models.Model):
    user = models.ForeignKey(User)
    grid_id = models.CharField(max_length=25)
    title = models.CharField(max_length=100)
    story = models.CharField(max_length=2500)

    def __unicode__(self):
        return self.title

class Choices(models.Model):
    choice = models.CharField(max_length=2500)
    belongs_to = models.ForeignKey(Narrative)

    def __unicode__(self):
        return self.choice

class Question(models.Model):
    question = models.TextField()

    def __unicode__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=500)
    attribute = models.CharField(max_length=50)

    def __unicode__(self):
        return self.answer

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(blank=True, max_length=20, choices=GENDER)
    age = models.IntegerField(blank=True, null=True)
    last_visit = models.DateTimeField(blank=True, null=True)
    hair = models.CharField(blank=True, max_length=50)
    
    def __unicode__(self):
        return self.user.username
