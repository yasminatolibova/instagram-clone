from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StoryViewSet

router = DefaultRouter()
router.register(r'stories', StoryViewSet, basename='story')
# router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls))
]
