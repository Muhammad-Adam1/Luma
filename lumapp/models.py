from django.db import models

from django.contrib.auth.models import AbstractUser
import uuid


class Team(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    team_name = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    project_name = models.CharField(max_length=100)
    is_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)  # Allow due date to be optional
    team = models.ForeignKey(Team, on_delete=models.CASCADE)  # ForeignKey to associate a project with a team

    def __str__(self):
        return self.project_name


class CustomUser(AbstractUser):
    English = 'English'
    German = 'German'
    French = 'French'
    English_US = 'English_US'
    Hindi = 'Hindi'

    STATUS_CHOICES = (
        (English, 'English'),
        (German, 'German'),
        (French, 'French'),
        (English_US, 'English_US'),
        (Hindi, 'Hindi'),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    full_name = models.CharField(max_length=60, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile-pics/', blank=True, null=True)
    job_role = models.CharField(max_length=50, blank=True, null=True)
    languages = models.CharField(max_length=20, choices=STATUS_CHOICES, default=English)
    team = models.OneToOneField(Team, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Custom User"

    def __str__(self):
        return str(self.username)

    def save(self, *args, **kwargs):
        # Update the full_name field before saving
        self.full_name = f'{self.first_name} {self.last_name}'
        if self.password:
            self.set_password(self.password)
        super().save(*args, **kwargs)

    @property
    def image_url(self):
        try:
            img = self.profile_pic.url
        except:
            img = ""
        return img


class Task(models.Model):
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'
    DO_LATER = 'Do Later'
    UPCOMING = 'Upcoming'

    STATUS_CHOICES = (
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
        (DO_LATER, 'Do Later'),
        (UPCOMING, 'Upcoming'),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    task_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=IN_PROGRESS)
    video_call = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='task_pics/', blank=True, null=True)
    is_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)  # Allow due date to be optional
    assigned_to = models.ManyToManyField(CustomUser, related_name='tasks_assigned', blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name


class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='sender')
    recipient = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='receiver')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, null=True)
    is_system_message = models.BooleanField(default=False)

    class Meta:
        # newer created messages will be at the top
        ordering = ['-timestamp']


class Chat(models.Model):
    participants = models.ManyToManyField(CustomUser, related_name='chats')
    last_message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True, blank=True)


class Notification(models.Model):
    content = models.TextField()
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=50)  # E.g., "Chat", "Task Due Date", "New Project", "New Task"
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.recipient}'

    class Meta:
        ordering = ['-timestamp']
