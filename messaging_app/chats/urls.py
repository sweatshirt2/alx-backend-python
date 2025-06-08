from django.urls import path
from .views import (
    UserProfileListCreateAPIView,
    ConversationListCreateAPIView,
    MessageListCreateAPIView,
)

urlpatterns = [
    path("api/users", UserProfileListCreateAPIView.as_view(), name="users_list_create"),
    path(
        "api/conversations",
        ConversationListCreateAPIView.as_view(),
        name="conversations_list_create",
    ),
    path(
        "api/messages", MessageListCreateAPIView.as_view(), name="messages_list_create"
    ),
]
