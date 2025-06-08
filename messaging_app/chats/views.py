from django.shortcuts import render
from rest_framework import generics, filters, viewsets, decorators, response
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
    # Todo: find a proper status code management for serializers
    status = 200 or 201


class ConversationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class MessageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # Todo: explore on filters
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # ? What is the below one, it was in the above list in chatgpts response and imported from django_filters.rest_framework
    # DjangoFilerBackend
    # ? I couldn't install it with pip, not find the package it is imported from


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    @decorators.action(detail=True, methods=["get"])
    def participants(self, request, pk=None):
        conversation = self.get_object()
        users = conversation.participants.all()
        return response.Response({"participants": users})
