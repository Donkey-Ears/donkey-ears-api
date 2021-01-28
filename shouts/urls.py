from rest_framework.routers import DefaultRouter
from .views import ShoutViewSet

app_name = "shouts"

router = DefaultRouter()
router.register("", ShoutViewSet)

urlpatterns = router.urls
