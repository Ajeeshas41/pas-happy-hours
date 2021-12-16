from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from team.models import Team

class Genre(models.Model):
    genre_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.genre_name

class Question(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,related_name='genre_question')
    title = models.CharField(max_length=30)
    question = models.TextField()
    answer = models.TextField(null=True, blank=True)
    image_enabled = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='question_pics', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_locked = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self):
        super().save()
        if self.image:
            img = Image.open(self.image.path)

            if img.width > 300 or img.height > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

class GenreTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='genre_team')
    score = models.IntegerField(default=0,null=True, blank=True)
    questions_attempted = models.IntegerField(default=0,null=True, blank=True)
    questions_answered = models.IntegerField(default=0,null=True, blank=True)
    sort_order = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.team.teamname

class Game(models.Model):
    round = models.IntegerField(default=0)
    team = models.ForeignKey(GenreTeam, on_delete=models.CASCADE, related_name='game_team')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='game_genre',null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='game_question',null=True, blank=True)
    answer = models.CharField(max_length=200, null=True, blank=True)
    override = models.BooleanField(default=False)
    is_submitted = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)
    won = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(null=True, blank=True)
    submitted_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='submited_user', null=True, blank=True)
    started_at = models.DateTimeField(null=True, blank=True)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return f'Round {self.round}: {self.team.team.teamname}'

# class Result(models.Model):
#     game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_result')


