from .views import dnaViewSet, simiosXHumanosViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'simian', dnaViewSet)
router.register(r'stats', simiosXHumanosViewSet)
urlpatterns = router.urls