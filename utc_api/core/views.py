from django.shortcuts import render
from rest_framework import viewsets
from core import serializers
from core import models


class TaskUserViewSet(viewsets.ModelViewSet):
    queryset = models.TaskUser.objects.all().order_by('name')
    serializer_class = serializers.TaskUserSerializer

class TaskStateViewSet(viewsets.ModelViewSet):
    queryset = models.TaskState.objects.all().order_by('id')
    serializer_class = serializers.TaskStateSerializer
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all().order_by('id')
    serializer_class = serializers.TaskSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.TaskDetailSerializer

        return self.serializer_class



    