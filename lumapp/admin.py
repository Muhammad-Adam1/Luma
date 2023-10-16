from django.contrib import admin

from .models import CustomUser, Chat, Project, Team, Task, Message, Notification

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Chat)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Task)
admin.site.register(Message)
admin.site.register(Notification)
