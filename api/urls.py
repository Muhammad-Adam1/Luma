from django.urls import path

from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # generate token for the user
    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # refresh the token for the user, so that the user can stay logged in
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # creating a new user
    path('user/create/', views.CustomUserCreateView.as_view(), name='user-create'),

    # retrieving and updating a user profile
    path('user/<uuid:pk>/', views.CustomUserRetrieveUpdateView.as_view(), name='user-retrieve-update'),

    # Deleting a user profile
    path('user-deletition/<uuid:pk>/', views.CustomUserDelete.as_view(), name='user-retrieve-update'),

    # creating and listing all the teams
    path('teams/', views.TeamList.as_view(), name='team-list'),

    # retrieving, updating and deleting the specific team
    path('team-detail/<uuid:pk>/', views.TeamDetails.as_view(), name='team-detail'),

    # creating and listing all the Projects
    path('projects/', views.ProjectList.as_view(), name='project-list'),

    # retrieving, updating and deleting the specific project
    path('projects/<uuid:pk>/', views.ProjectDetails.as_view(), name='project-detail'),

    # creating and listing all the Tasks
    path('tasks/', views.TaskList.as_view(), name='task-list'),

    # retrieving, updating and deleting the specific project
    path('tasks/<uuid:pk>/', views.TaskDetails.as_view(), name='task-detail'),

]
