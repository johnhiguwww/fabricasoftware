from rest_framework.viewsets import ModelViewSet
from apps.todo.models import Task
from .serializers import TaskSerializer

class TaskViewSet(ModelViewSet):
    #Quero todos os dados que estão ma tabela "Task"
    queryset = Task.objects.all()

    serializer_class = TaskSerializer