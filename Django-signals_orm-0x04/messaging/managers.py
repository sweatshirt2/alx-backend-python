from django.db import models
from django.contrib.auth.models import User


class UnreadMessagesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def unread(self):
        """get Message instances with unread True

        Kwargs:
        None

        Return: unread messages
        """
        return self.get_queryset().filter(unread=True)

    def unread_for_user(self, user: User):
        """get Message instances with unread True and a specific receiver user

        Kwargs:
        user -- the current logged in user

        Return: unread messages for a specific user
        """
        return self.get_queryset().filter(receiver=user)
