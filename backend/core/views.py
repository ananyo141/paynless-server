# Create your views here.
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from .models import User
from .permissions import IsSameUser
from .serializers import UserProfileSerializer, UserSerializer


# User views
class UserList(ListCreateAPIView):
    """
    List all users, or create a new user.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserProfileSerializer  # return elaborate details while creating
        return UserSerializer


class UserProfile(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, or modify a user's profile.
    """

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsSameUser]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user
