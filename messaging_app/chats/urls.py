from django.urls import path, include  # Todo: explore how include can be used here
from .views import (
    UserProfileListCreateAPIView,
    ConversationListCreateAPIView,
    MessageListCreateAPIView,
    # Todo: explore these and how they have been setup in .views
    ConversationViewSet,
    MessageViewSet,
)

# Todo: explore how these could be used here
# from rest_framework import routers
# routers.DefaultRouter()

# Todo: explore (no idea what it is)
# NestedDefaultRouter

urlpatterns = [
    path("users", UserProfileListCreateAPIView.as_view(), name="users_list_create"),
    path(
        "conversations",
        ConversationListCreateAPIView.as_view(),
        name="conversations_list_create",
    ),
    path("messages", MessageListCreateAPIView.as_view(), name="messages_list_create"),
]
