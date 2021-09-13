"""View module for handling requests for routines"""
from django.http import HttpResponseServerError
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from tabtrackerapi.models import Routine
from rest_framework import status


class RoutineView(ViewSet):
    """Tab Tracker Routines"""
    def list(self, request, pk=None):
        """Handle GET requests for all routines

        Returns:
            Response -- JSON serialized routine
        """
        try:
            routines = Routine.objects.filter(user=request.auth.user)

            serializer = RoutineSerializer(
                routines, many=True, context={'request': request})
            
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single routine

        Returns:
            Response -- JSON serialized routine
        """
        try:
            routine = Routine.objects.get(pk=pk)
            serializer = RoutineSerializer(
                routine, many=False, context={'request': request})

            return Response(serializer.data)
        
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        """Handles POST requests for routines
        Returns:
            Response -- JSON serialized routine data
        """

        try:
            routine = Routine.objects.create(
                user = request.auth.user,
                routine_name = request.data['routine_name'],
                description = request.data['description'],
            )
            serializer = RoutineSerializer(
                routine, many=False, context={'request': request}
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Handles PUT requests for routine
        Returns:
            Response -- Empty body with 204 status
        """

        try: 
            routine = Routine.objects.get(pk=pk)

            routine.user = request.auth.user
            routine.routine_name = request.data['routine_name']
            routine.description = request.data['description']
            routine.save()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

class RoutineSerializer(serializers.ModelSerializer):
    """JSON serializer for routines

    Arguments:
        serializers
    """
    class Meta:
        model = Routine
        fields = ('id', 'user', 'routine_name', 'description')
