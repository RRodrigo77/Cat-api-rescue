from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import CatsViewSet

router = DefaultRouter()
router.register(r'cats', CatsViewSet)

urlpatterns = router.urls
