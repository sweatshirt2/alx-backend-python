from django.urls import path
from .views import (
    UserProfileListCreateAPIView,
    ConversationListCreateAPIView,
    MessageListCreateAPIView,
)

urlpatterns = [
    path("users", UserProfileListCreateAPIView.as_view(), name="users_list_create"),
    path(
        "conversations",
        ConversationListCreateAPIView.as_view(),
        name="conversations_list_create",
    ),
    path("messages", MessageListCreateAPIView.as_view(), name="messages_list_create"),
]
