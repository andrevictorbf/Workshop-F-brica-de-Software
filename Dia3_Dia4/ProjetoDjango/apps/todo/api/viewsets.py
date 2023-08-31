from rest_framework.viewsets import ModelViewSet

from apps.todo.models import Task

from .serializers import TaskSerializer
"""todos os dados da tabela que estão na Tabela task"""
class TaskViewSet (ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer