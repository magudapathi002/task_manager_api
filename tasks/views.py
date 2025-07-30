from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsAdminOrTaskOwner

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = request.user
    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "is_staff": user.is_staff,
        "is_superuser": user.is_superuser,
        "groups": list(user.groups.values_list('name', flat=True)),
        "permissions": list(user.get_all_permissions())
    })

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminOrTaskOwner]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['priority', 'due_date', 'assigned_to', 'status']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

