from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.decorators.cache import cache_page

from .models import Message


class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request: Request, *args):
        user = request.user
        user.delete()

        return Response(
            {"detail": "Account removed successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["DELETE"])
def delete_user(request: Request):
    if request.method == "DELETE":
        request.user.delete()
        return Response(
            {"detail": "Account removed successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET"])
@cache_page(60)
def message_list(request: Request):
    """get list of messages with their senders and receivers loaded | avoids N+1 queries

    Kwargs:
    None

    Return: list of messages with their sender and receiver
    """

    """cached view for 60 seconds"""
    if request.method == "GET":
        messages = Message.objects.filter(
            Q(receiver=request.user) | Q(sender=request.user)
        ).select_related("sender", "receiver")

        return Response({"messages": messages}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET"])
def message_detail(request: Request, pk: int):
    if request.method == "GET":
        message_with_replies = (
            Message.objects.select_related("sender", "receiver", "parent_message")
            .prefetch_related("replies")
            .get(pk=pk)
        )
        return Response({"messages": message_with_replies}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET"])
def unread_messages(request: Request):
    if request.method == "GET":
        unread_messages = (
            Message.unread.unread_for_user(request.user)
            .only("content")
            .select_related("sender")
        )

        return Response({"unread_messages": unread_messages}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
