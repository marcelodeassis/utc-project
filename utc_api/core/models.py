from django.db import models

class TaskUser(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TaskState(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    description = models.CharField(max_length=100)
    state = models.ForeignKey(TaskState, on_delete=models.CASCADE)
    user = models.ForeignKey(TaskUser, on_delete=models.CASCADE)

    def __str__(self):
        return " | ".join([self.description, self.state.name, self.user.name])


