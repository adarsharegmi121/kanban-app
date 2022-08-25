from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from kanban_lane.models import KanbanLane
from kanban_lane.serializers import KanbanLaneSerializer
from user_login.decorator import authorize


class KanbanLaneAPIView(APIView):
    # list all the lanes
    @authorize()
    def get(self, request, *args, **kwargs):
        """
        list lanes
        """
        lanes = KanbanLane.objects.all()
        serializer = KanbanLaneSerializer(lanes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @authorize()
    def post(self, request, *args, **kwargs):
        """
        register the kanban KanbanLane
        """
        data = {
            "lane_name": request.data.get("lane_name"),
            "lane": request.data.get("lane")
        }
        serializer = KanbanLaneSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KanbanLaneDetailView(APIView):
    @authorize()
    def get(self, request, lane_id, *args, **kwargs):
        """
        list the specific lane
        """
        try:
            lane = KanbanLane.objects.get(id=lane_id)
            serializer = KanbanLaneSerializer(lane)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except KanbanLane.DoesNotExist:
            return Response(
                {"res": "no lane found"}, status=status.HTTP_400_BAD_REQUEST
            )

    @authorize()
    def put(self, request, lane_id, *args, **kwargs):
        """
        update the kanban lane details
        """
        lane_instance = KanbanLane.objects.get(id=lane_id)
        if not lane_instance:
            return Response(
                {"res": "no lane found for the lane id"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = {
            "lane_name": request.data.get("lane_name"),
            "board": request.data.get("board")
        }
        serializer = KanbanLaneSerializer(instance=lane_instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @authorize()
    def delete(self, request, lane_id, *args, **kwargs):
        """
        delete the lane
        """
        lane_instance = KanbanLane.objects.get(id=lane_id)
        if not lane_instance:
            return Response(
                {"res": "object with lane id not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        lane_instance.delete()
        return Response({"res": "lane is deleted"}, status=status.HTTP_200_OK)
