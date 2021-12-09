from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Team(models.Model):
    teamname = models.CharField(max_length=100)
    usercount = models.IntegerField(blank=True, default=1)
    is_active = models.BooleanField(default=True)
    level = models.IntegerField(null=True, blank=True)
    securitykey = models.CharField(max_length=15)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    

    def __str__(self):
        return self.teamname
    
    def get_absolute_url(self):
        return reverse('team-details', kwargs={'pk':self.pk})

class Participant(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='participants', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name

