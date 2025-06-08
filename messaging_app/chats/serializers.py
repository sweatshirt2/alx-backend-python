from rest_framework import serializers
from .models import UserProfile, Conversation, Message


class UserProfileSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(
        max_length=500,
        allow_blank=True,
        required=False,
        help_text="A short description of the user.",
    )

    class Meta:
        model = UserProfile
        fields = [
            "user_id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "bio",
        ]

    def validate(self, data):
        first_name = data.get(
            "first_name", self.instance.first_name if self.instance else None
        )
        last_name = data.get(
            "last_name", self.instance.last_name if self.instance else None
        )

        if "first_name" not in data:
            raise serializers.ValidationError(
                {"first_name": "First name is required"}, code="first_name_missing"
            )

        if "last_name" not in data:
            raise serializers.ValidationError(
                {"last_name": "Last name is required"}, code="last_name_missing"
            )

        # if first_name and last_name and first_name.lower() == last_name.lower():
        #     raise serializers.ValidationError(
        #         "First name and last name cannot be the same.",
        #         code="names_identical",
        #     )

        if "bio" in data and not data.get("tagline"):
            raise serializers.ValidationError(
                {"tagline": "Tagline is required when updating the bio."},
                code="tagline_missing",
            )

        return data


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserProfileSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    message_count = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = "__all__"

    def get_message_count(self, obj):
        return obj.messages.count()
