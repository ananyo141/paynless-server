from rest_framework.serializers import ModelSerializer

from .models import Role, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"required": True},
            "email": {"write_only": True},
            "role": {"write_only": True},
        }

        fields = ("id", "username", "role", "email", "name", "password")

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            name=validated_data["name"],
            username=validated_data["username"],
            role=validated_data.get("role", Role.CLIENT.value),
        )
        # identify password field to be set as hashed password
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserProfileSerializer(UserSerializer):
    """
    Return user profile with posts and additional details.
    """

    class Meta:
        model = User
        extra_kwargs = {"password": {"write_only": True}}
        fields = ("id", "username", "role", "email", "name", "password")
