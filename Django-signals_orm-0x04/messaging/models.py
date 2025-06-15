from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    parent_message = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True, related_name="replies"
    )
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_messages"
    )
    content = models.TextField()
    edited = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    message = models.OneToOneField(
        Message, on_delete=models.CASCADE, related_name="message_notification"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )


class MessageHistory(models.Model):
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="versions"
    )
    edited_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="edited_messages"
    )
    content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)
