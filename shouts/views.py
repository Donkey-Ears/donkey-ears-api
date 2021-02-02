from .models import Shout
from .serializers import ShoutSerializer
from .permissions import IsAuthor
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet


class ShoutViewSet(ModelViewSet):
    queryset = Shout.objects.select_related("user").all()
    serializer_class = ShoutSerializer

    def get_permissions(self):
        if (
            self.action == "list"
            or self.action == "retrieve"
            or self.action == "destroy"
            or self.action == "update"
        ):
            permission_classes = [IsAuthor | permissions.IsAdminUser]
        elif self.action == "create":
            permission_classes = [permissions.IsAuthenticated | permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = super().get_queryset()
        else:
            queryset = super().get_queryset().filter(user=self.request.user)
        return queryset
