from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import ApplicantProfile


@receiver(post_save, sender=User)
def create_applicant_profile(sender, instance, created, **kwargs):
    if created:
        ApplicantProfile.objects.create(user=instance)
