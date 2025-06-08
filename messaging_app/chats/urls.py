from django.urls import path, include  # Todo: explore how include can be used here
from .views import (
    UserProfileListCreateAPIView,
    ConversationListCreateAPIView,
    MessageListCreateAPIView,
)

# Todo: explore how these could be used here
# from rest_framework import routers
# routers.DefaultRouter()

urlpatterns = [
    path("users", UserProfileListCreateAPIView.as_view(), name="users_list_create"),
    path(
        "conversations",
        ConversationListCreateAPIView.as_view(),
        name="conversations_list_create",
    ),
    path("messages", MessageListCreateAPIView.as_view(), name="messages_list_create"),
]
