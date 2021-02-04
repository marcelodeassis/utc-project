from rest_framework import serializers

from core import models

class TaskUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TaskUser
        fields = ('id', 'name',)

class TaskStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TaskState
        fields = ('id', 'name')
        read_only_fields = ('id',)

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    state = serializers.PrimaryKeyRelatedField(
        queryset=models.TaskState.objects.all(),
    )

    user = serializers.PrimaryKeyRelatedField(
        queryset=models.TaskUser.objects.all(),
    )

    class Meta:
        model = models.Task
        fields = ('id', 'description', 'state', 'user')
        read_only_fields = ('id',)

class TaskDetailSerializer(TaskSerializer):
    state = TaskStateSerializer(read_only=True)
    user = TaskUserSerializer(read_only=True)