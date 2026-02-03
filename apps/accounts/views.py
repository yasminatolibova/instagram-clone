from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from .models import Profile
from .serializers import RegisterSerializer, ProfileSerializers, UserSerializer
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