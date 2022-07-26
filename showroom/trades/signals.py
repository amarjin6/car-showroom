from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import UserProfile
from trades.models import Balance


@receiver(post_save, sender=UserProfile)
def create_profile_related_attributes(sender, instance, created, **kwargs):
    if created:
        Balance.objects.create(user=instance)
