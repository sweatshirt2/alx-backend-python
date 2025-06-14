from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Message, Notification, MessageHistory


@receiver(post_save, sender=Message)
def message_received(sender, instance: Message, created, **kwargs):
    """triggers creating a notification when a message is sent to a user

    Kwargs:
    instance -- an instance of message
    created -- whether the message is new

    Return: None
    """

    if created:
        Notification.objects.create(message=instance, user=instance.receiver)


@receiver(pre_save, sender=Message)
def message_edited(sender, instance: Message, created, **kwargs):
    """triggers creating a message history, logging message, editor information when a message is edited

    Kwargs:
    instance -- an instance of message
    created -- whether the message is new

    Return: None
    """
    if not created:
        old_message = Message.objects.get(pk=instance.pk)
        MessageHistory.objects.create(
            message=instance, edited_by=instance.sender, content=instance.content
        )
        # message_history = instance.versions.all()
        message_history = MessageHistory.objects.filter(message=instance)

        for version in message_history:
            print(version.content, version.edited_at)
