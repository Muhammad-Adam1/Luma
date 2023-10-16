from django.urls import path

from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # generate token for the user
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # refresh the token for the user, so that the user can stay logged in
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # creating a new user
    path('user/create/', views.CustomUserCreateView.as_view(), name='user-create'),

    # retrieving and updating a user profile
    path('user/<uuid:pk>/', views.CustomUserRetrieveUpdateView.as_view(), name='user-retrieve-update'),

    # retrieving all the teams
    path('teams/', views.TeamList.as_view(), name='team-list'),

    # retrieving all the Projects
    path('projects/', views.ProjectList.as_view(), name='team-list'),

    # retrieving, updating or deleting a specific project
    path('Project/<uuid:pk>/', views.ProjectDetail.as_view(), name='team-list'),

]
