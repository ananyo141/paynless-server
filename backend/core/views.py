# Create your views here.
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.views import Response

from .models import User
from .permissions import IsSameUser
from .serializers import UserProfileSerializer


# OAuth views
class OAuthCreate(CreateAPIView):
    """
    Create the user from the oauth provider.
    post request:
     - id
     - email
     - name
     - avatar url
    """

    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def perform_create(self, serializer):
        user = User(**serializer.validated_data)
        accessToken = AccessToken.for_user(user)
        return str(accessToken)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        accessToken = self.perform_create(serializer)
        return Response(
            {"access_token": accessToken},
            status=201,
        )


class OAuthProfile(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, or modify a user's profile.
    """

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsSameUser]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user
