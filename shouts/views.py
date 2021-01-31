from rest_framework.viewsets import ModelViewSet
from .models import Shout
from .serializers import ShoutSerializer
from .permissions import IsAuthor
from rest_framework.permissions import IsAdminUser


class ShoutViewSet(ModelViewSet):
    queryset = Shout.objects.select_related("user").all()
    serializer_class = ShoutSerializer
    permission_classes = [IsAuthor, IsAdminUser]
