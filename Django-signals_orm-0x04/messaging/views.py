from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User


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
