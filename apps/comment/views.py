from django.shortcuts import render
from rest_framework import viewsets,  permissions, status
from .models import Comment, CommentLike
from .serializers import CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class=CommentSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        queryset=Comment.objects.all()
        post_id=self.request.query_params.get('post')

        reel_id=self.request.query_params.get('reels')

        story_id=self.request.query_params.get('story')

        if post_id:
            queryset=queryset.filter(post_id=post_id)

        if reel_id:
            queryset=queryset.filter(reels_id=reel_id)

        if story_id:
            queryset=queryset.filter(story_id=story_id)

        return queryset


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        comment = self.get_object()
        user = request.user

        like, created = CommentLike.objects.get_or_create(user=user, comment=comment)

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
    

    
    

