from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    bio = models.TextField(blank=True)
    pass


class Conversation(models.Model):
    first_user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="first_user"
    )
    second_user_id = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="second_user"
    )


class Message(models.Model):
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
