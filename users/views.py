import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["post"])
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user is not None:
            encoded_jwt = jwt.encode(
                {"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256"
            )
            return Response(data={"token": encoded_jwt, "id": user.pk})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=True, methods=["get"])
    def profile(self, request, pk=None):
        """ Profile View. """
        many = False

        if request.user.is_superuser:
            # Superuser의 경우 모든 프로필을 볼 수 있음.
            user = super().get_queryset()
            many = True
        else:
            # admin이 아닌 경우 본인의 프로필만 볼 수 있음.
            user = request.user
        data = UserSerializer(user, many=many).data
        return Response(data, status=status.HTTP_200_OK)

    def logout(self, request):
        pass
