from django.contrib import admin
from .models import TaskUser, TaskState, Task

admin.site.register(TaskUser)
admin.site.register(TaskState)
admin.site.register(Task)
