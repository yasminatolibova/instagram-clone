from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Reel, Like
from .serializers import ReelSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.



class ReelViewSet(viewsets.ModelViewSet):
    queryset = Reel.objects.filter(is_public=True)
    serializer_class = ReelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    search_fields = ['tags', 'caption', 'user__username']
    ordering_fields = ['created_at', 'views_count']
    ordering = ['-created_at']

    def retrieve(self, request, *args, **kwargs):
        reel = self.get_object()
        reel.views_count += 1
        reel.save(update_fields=['views_count'])
        return super().retrieve(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        reel = self.get_object()
        user = request.user

        like, created = Like.objects.get_or_create(user=user, reel=reel)

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
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     def get_queryset(self):
#         reel_id = self.request.query_params.get('reel')

#         if reel_id:
#             return Comment.objects.filter(reels_id=reel_id)
#         return Comment.objects.all()
    

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
    
