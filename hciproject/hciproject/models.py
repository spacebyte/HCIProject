from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django_mysql.models import JSONField

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    score = JSONField(default='{"T": 0, "L": 0, "P": 0, "H": 0, "B": 0}')
    number_of_questions = JSONField(default='{"T": 0, "L": 0, "P": 0, "H": 0}')
    total_score = models.IntegerField(default=0)
    quizes_played = models.IntegerField(default=0)
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
