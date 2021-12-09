from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Team, Participant

@receiver(post_save, sender=Participant)
def update_usercount(instance, **kwargs):
    if instance.team:
        c = Participant.objects.filter(team=instance.team).count()
        team = Team.objects.get(pk=instance.team.id)
        team.usercount = c
        team.save()

@receiver(post_save, sender=User)
def create_user_participant(instance, created, **kwargs):
    if created:
        Participant.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_participant(instance, **kwargs):
    instance.participant.save()