from django.shortcuts import render
from rest_framework import generics
from .models import UserProfile, Conversation, Message
from .serializers import (
    UserProfileSerializer,
    ConversationSerializer,
    MessageSerializer,
)


# Create your views here.
class UserProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ConversationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class MessageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
