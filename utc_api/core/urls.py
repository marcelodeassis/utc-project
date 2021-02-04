from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'task_states', views.TaskStateViewSet, basename='task_states')
router.register(r'task_users', views.TaskUserViewSet, basename='task_users')
router.register(r'tasks', views.TaskViewSet, basename='task')


urlpatterns = [
    path('', include((router.urls, 'core'))),
    #path('api-auth/', include('rest_framework.urls', namespace='core'))
]
