from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import *

router = DefaultRouter()

router.register('tags', TagApiViewSet)
router.register('users', UserApiViewSet)
router.register('posts', PostApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]