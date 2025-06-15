from django.db import models
from django.contrib.auth.models import User


class UnreadMessagesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def unread(self):
        return self.get_queryset().filter(unread=True)

    def unread_for_user(self, user: User):
        return self.get_queryset().filter(receiver=user)
