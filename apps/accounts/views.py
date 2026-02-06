from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Profile, Follow
from .serializers import RegisterSerializer, ProfileSerializers, UserSerializer, FollowSerializer, UserListSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user).data,
            'message': 'User muvaffaqiyatli royhatdan otdi'
        }, status=status.HTTP_201_CREATED
        )
    
class ProfileRetrievUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


    def get_object(self):
        user_id = self.kwargs.get('pk')
        if user_id:
            return Profile.objects.get(user_id=user_id)
        return self.request.user.profile
    
class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)

        if user_to_follow == request.user:
            return Response(
                {
                    'error': "O'zizga follow qila olmaysiz"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if Follow.objects.filter(follower=request.user, following=user_to_follow).exists():
            return Response(
                {
                    'error': "Siz bu userni allaqachon follow qilgansiz"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        follow = Follow.objects.create(
            follower=request.user,
            following=user_to_follow
        )

        serializer = FollowSerializer(follow)

        return Response(
            {
                'message': f"{user_to_follow} muvaffaqiyatli follow qilindi",
                'follow': serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    

class UnFollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)

        try:
            follow = Follow.objects.get(
                follower=request.user,
                following=user_to_unfollow
            )
            follow.delete()
            return Response(
                {
                    'message': f"{user_to_unfollow.username} unfollow qilindi"
                },
                status=status.HTTP_200_OK
            )
        
        except Follow.DoesNotExist:
            return Response(
                {
                    'error': 'Siz bu userni follow qilmagansiz'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        

class FollowersListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(User, id=user_id)
        follower_ids = Follow.objects.filter(following=user).values_list('follower', flat=True)
        return User.objects.filter(id__in=follower_ids)
    


class FollowingListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(User, id=user_id)
        following_ids = Follow.objects.filter(follower=user).values_list('following', flat=True)
        return User.objects.filter(id__in=following_ids)