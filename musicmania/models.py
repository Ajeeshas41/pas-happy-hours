from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

from team.models import Team

class Genre(models.Model):
    genre_name = models.CharField(max_length=30)
    is_active = models.BooleanField()

    def __str__(self):
        return self.genre_name


class Question(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE(), related_name='genre_question')
    question = models.TextField()
    is_active = models.BooleanField()
    is_locked = models.BooleanField(default=False)

    def __str__(self):
        return self.question

class Game(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE(), related_name='game_question')
    team = models.ForeignKey(Team, on_delete=models.CASCADE(), related_name='game_team')
    answer = models.CharField(max_length=200, null=True)
    override = models.BooleanField(default=False)
    is_submitted = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(null=True, blank=True)
    submitted_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='submited_user', null=True, blank=True)
    time_taken = models.IntegerField(default=18000)