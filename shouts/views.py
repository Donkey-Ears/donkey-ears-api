from rest_framework.viewsets import ModelViewSet
from .models import Shout
from .serializers import ShoutSerializer


class ShoutViewSet(ModelViewSet):
    queryset = Shout.objects.select_related("user").all()
    serializer_class = ShoutSerializer
