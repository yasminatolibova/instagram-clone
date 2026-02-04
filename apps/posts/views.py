from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like, Comment
from .serializers import PostSerializer, UserSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user

        like, created = Like.objects.get_or_create(user=user, post=post)

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
    

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.request.query_params.get('post')

        if post_id:
            return Comment.objects.filter(post_id=post_id)
        return Comment.objects.all()
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)