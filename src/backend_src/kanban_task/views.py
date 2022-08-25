from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from kanban_task.models import KanbanTask
from kanban_task.serializers import KanbanTaskSerializer
from user_login.decorator import authorize


class KanbanTaskAPIView(APIView):
    # list all the tasks
    @authorize()
    def get(self, request, *args, **kwargs):
        """
        list tasks
        """
        tasks = KanbanTask.objects.all()
        serializer = KanbanTaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @authorize()
    def post(self, request, *args, **kwargs):
        """
        register the KanbanTask
        """
        data = {
            "title": request.data.get("title"),
            "description": request.data.get("description"),
            "status": request.data.get("status"),
            "lane": request.data.get("lane"),
        }
        serializer = KanbanTaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KanbanTaskDetailView(APIView):
    @authorize()
    def get(self, request, task_id, *args, **kwargs):
        """
        list the specific task
        """
        try:
            task = KanbanTask.objects.get(id=task_id)
            serializer = KanbanTaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except KanbanTask.DoesNotExist:
            return Response(
                {"res": "no task found"}, status=status.HTTP_400_BAD_REQUEST
            )

    @authorize()
    def put(self, request, task_id, *args, **kwargs):
        """
        update the kanban task details
        """
        task_instance = KanbanTask.objects.get(id=task_id)
        if not task_instance:
            return Response(
                {"res": "no task found for the task id"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = {
            "title": request.data.get("title"),
            "description": request.data.get("description"),
            "status": request.data.get("status"),
            "lane": request.data.get("lane"),
        }
        serializer = KanbanTaskSerializer(instance=task_instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @authorize()
    def delete(self, request, task_id, *args, **kwargs):
        """
        delete the task
        """
        task_instance = KanbanTask.objects.get(id=task_id)
        if not task_instance:
            return Response(
                {"res": "object with task id not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        task_instance.delete()
        return Response({"res": "task is deleted"}, status=status.HTTP_200_OK)
