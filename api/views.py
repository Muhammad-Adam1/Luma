from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

# serializers
from .serializers import (CustomUserSerializer, TaskSerializer, MessageSerializer, ChatSerializer,
                          NotificationSerializer, TeamSerializer, ProjectSerializer)
# models
from lumapp.models import CustomUser, Task, Message, Chat, Notification, Team, Project


# user creation api
class CustomUserCreateView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer


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
        user_id = self.kwargs['id']
        return get_object_or_404(CustomUser, id=user_id)


# getting Teams from the DataBase
class TeamList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]


# getting list of Projects from the DataBase
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


# getting specific project details from the DataBase
class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # we can filter projects by team or any other criteria, For example, filter by team id
        team_id = self.kwargs['id']
        return get_object_or_404(Project, team__id=team_id)


