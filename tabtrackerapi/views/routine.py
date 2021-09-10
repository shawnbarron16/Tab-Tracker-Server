"""View module for handling requests for routines"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from tabtrackerapi.models import Routine

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

class RoutineSerializer(serializers.ModelSerializer):
    """JSON serializer for routines

    Arguments:
        serializers
    """
    class Meta:
        model = Routine
        fields = ('id', 'user', 'routine_name', 'description')
