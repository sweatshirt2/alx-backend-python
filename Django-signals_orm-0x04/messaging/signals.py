from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

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
def message_edited(sender, instance: Message, **kwargs):
    """triggers creating a message history, logging message, editor information when a message is edited

    Kwargs:
    instance -- an instance of message
    created -- whether the message is new

    Return: None
    """
    if not instance.pk:
        return
    try:
        old_message = Message.objects.get(pk=instance.pk)
    except Message.DoesNotExist:
        return

    if instance.content == old_message.content:
        return

    MessageHistory.objects.create(
        message=instance, edited_by=instance.sender, content=old_message.content
    )
    instance.edited = True
    # message_history = instance.versions.all()
    message_history = MessageHistory.objects.filter(message=instance)
    for version in message_history:
        print(version.content, version.edited_at)


@receiver(post_delete, sender=User)
def user_deleted(sender, instance: User, **kwargs):
    Message.objects.filter(user=instance).delete()
