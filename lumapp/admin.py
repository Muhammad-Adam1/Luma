from django.contrib import admin

from .models import CustomUser, Project, Team, Task, Chat, Message, Notification

admin.site.register(CustomUser)
admin.site.register(Chat)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Task)
admin.site.register(Message)
admin.site.register(Notification)
