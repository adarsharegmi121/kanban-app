from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from kanban_user.models import KanbanUser
from kanban_user.serializers import KanbanUserSerializer
from user_login.decorator import authorize


class KanbanUserAPIView(APIView):
    # list all the boards
    @authorize()
    def get(self, request, *args, **kwargs):
        """
        list boards
        """
        k_users = KanbanUser.objects.all()
        serializer = KanbanUserSerializer(k_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @authorize()
    def post(self, request, *args, **kwargs):
        """
        register the kanban KanbanUser
        """
        data = {"group_name": request.data.get("group_name"),
                "users":request.data.get('users'),
                "date_created":request.data.get('date_created')}
        print("data >>>>>>>>>>" ,data)
        serializer = KanbanUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KanbanUserDetailView(APIView):
    @authorize()
    def get(self, request, group_id, *args, **kwargs):
        """
        list the specific board
        """
        try:
            board = KanbanUser.objects.get(id=group_id)
            serializer = KanbanUserSerializer(board)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except KanbanUser.DoesNotExist:
            return Response(
                {"res": "no board found"}, status=status.HTTP_400_BAD_REQUEST
            )

    @authorize()
    def put(self, request, group_id, *args, **kwargs):
        """
        update the kanban board details
        """
        board_instance = KanbanUser.objects.get(id=group_id)
        if not board_instance:
            return Response(
                {"res": "no board found for the board id"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = {"group_name": request.data.get("group_name"),
                "users":request.data.get('users'),
                "date_created":request.data.get('date_created')}
        serializer = KanbanUserSerializer(instance=board_instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @authorize()
    def delete(self, request, group_id, *args, **kwargs):
        """
        delete the board
        """
        board_instance = KanbanUser.objects.get(id=group_id)
        if not board_instance:
            return Response(
                {"res": "object with board id not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        board_instance.delete()
        return Response({"res": "board is deleted"}, status=status.HTTP_200_OK)
