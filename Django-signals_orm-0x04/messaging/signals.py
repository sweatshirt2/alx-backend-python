from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Message, Notification


@receiver(post_save, sender=Message)
def message_received(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(message=instance, user=instance.receiver)
