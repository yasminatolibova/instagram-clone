from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Story, Like
from .serializers import StorySerializer,  UserSerializer
from .permissions import IsOwnerOrReadOnly
from django.utils import timezone
from datetime import timedelta



class StoryViewSet(viewsets.ModelViewSet):
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Story.objects.filter(
            created_at__gte=timezone.now() - timedelta(hours=24)
        )

    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def view_story(self, request, pk=None):
        story = self.get_object()
        story.views.add(request.user)
        return Response({'status': 'viewed'})
    
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        story = self.get_object()
        user = request.user

        like, created = Like.objects.get_or_create(user=user, story=story)

        if not created:
            like.delete()
            return Response({
                'status': 'unliked'
            }, status=status.HTTP_200_OK
            )
        return Response({
            'status': 'liked'
        }, status=status.HTTP_201_CREATED
        )
    

# class CommentViewSet(viewsets.ModelViewSet):
#     queryset=Comment.objects.all()
#     # serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     def get_queryset(self):
#         story_id = self.request.query_params.get('story')

#         if story_id:
#             return Comment.objects.filter(story_id=story_id)
#         return Comment.objects.all()
    

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
    
