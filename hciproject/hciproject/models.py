from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django_mysql.models import JSONField

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    score = JSONField()
    LOCATIONS = (
        ('C', 'City Centre'),
        ('W', 'West'),
        ('N', 'North'),
        ('E', 'East'),
        ('S', 'South')
    )
    location = models.CharField(max_length=1, choices=LOCATIONS, default='C')
    def __unicode__(self):
        return self.user.username


class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    answers = JSONField()
    question = models.CharField(max_length=255)
    image = models.ImageField(upload_to='question_images', blank=True)
    CATEGORIES = (
        ('L', 'Location'),
        ('T', 'Trivia'),
        ('H', 'History'),
        ('P', 'People'),
    )
    category = models.CharField(max_length=1, choices=CATEGORIES, default='T')
    learn_text = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return self.question
