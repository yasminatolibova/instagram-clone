from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView,
    ProfileRetrievUpdateView,
    FollowUserView,
    UnFollowUserView,
    FollowersListView,
    FollowingListView
    )


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('profile/', ProfileRetrievUpdateView.as_view(), name='profile'),
    path('profile/<int:pk>/', ProfileRetrievUpdateView.as_view(), name='profile_detail'),

    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnFollowUserView.as_view(), name='unfollow_user'),

    path('followers/<int:user_id>/', FollowersListView.as_view(), name='followers_list'),
    path('following/<int:user_id>/', FollowingListView.as_view(), name='following_list'),

]
