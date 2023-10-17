from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

# serializers
from .serializers import (CustomUserSerializer, TaskSerializer, MessageSerializer, ChatSerializer,
                          NotificationSerializer, TeamSerializer, ProjectSerializer, UserCreationSerializer )
# models
from lumapp.models import CustomUser, Task, Message, Chat, Notification, Team, Project


# user creation api
class CustomUserCreateView(generics.CreateAPIView):
    serializer_class = UserCreationSerializer


# getting user from the DataBase or updating the current user
class CustomUserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]


# Delete the specific user
class CustomUserDelete(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs['pk']
        return get_object_or_404(CustomUser, id=user_id)


# Team creation and listing out
class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]


# Retrieving, updating and destroying the specific Team
class TeamDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]


# Project creation and listing out
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


# Retrieving, updating and destroying the Project
class ProjectDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


# Project creation and listing out
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


# Retrieving, updating and destroying the Task
class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]



