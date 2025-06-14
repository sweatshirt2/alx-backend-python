from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Message, Notification


@receiver(post_save, sender=Message)
def message_received(sender, instance, created, **kwargs):
    """triggers creating a notification when a message is sent to a user

    Kwargs:
    instance -- an instance of message
    created -- whether the message is new

    Return: return_description
    """

    if created:
        Notification.objects.create(message=instance, user=instance.receiver)
