from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import EditorViewSet

router = DefaultRouter()
router.register("editor", EditorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
