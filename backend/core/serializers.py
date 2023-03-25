from rest_framework.serializers import ModelSerializer

from .models import Role, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {
            "id": {"required": True, "read_only": True},
            "password": {"write_only": True},
            "email": {"write_only": True},
            "role": {"write_only": True, "read_only": True},
        }

        fields = ("id", "role", "email", "name", "avatarUrl")

    def create(self, validated_data):
        user = User(
            id=validated_data["id"],
            email=validated_data["email"],
            name=validated_data["name"],
            avatarUrl=validated_data["avatarUrl"],
            username=validated_data["email"],
            role=validated_data.get("role", Role.USER.value),
        )
        user.set_password(validated_data["email"])
        user.save()
        return user


class UserProfileSerializer(UserSerializer):
    """
    Return user profile with posts and additional details.
    """

    class Meta:
        model = User
        extra_kwargs = {
            "id": {"required": True},
            "password": {"write_only": True},
        }
        fields = ("id", "role", "email", "name", "avatarUrl")
