"""View module for handling requests for exercises"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from tabtrackerapi.models import Exercise

class ExerciseView(ViewSet):
    """Tab Tracker Exercises"""
    def list(self, request, pk=None):
        """Handle GET requests for all exercises

        Returns:
            Response -- JSON serialized exercise
        """
        try:
            exercises = Exercise.objects.all()
            selected_routine = request.query_params.get('routine', None)

            if selected_routine is not None:
                exercises = exercises.filter(routine=selected_routine)

            serializer = ExerciseSerializer(
                exercises, many=True, context={'request': request})
            
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single exercise

        Returns:
            Response -- JSON serialized exercise
        """
        try:
            exercise = Exercise.objects.get(pk=pk)
            serializer = ExerciseSerializer(
                exercise, many=False, context={'request': request})

            return Response(serializer.data)
        
        except Exception as ex:
            return HttpResponseServerError(ex)

class ExerciseSerializer(serializers.ModelSerializer):
    """JSON serializer for exercises

    Arguments:
        serializers
    """
    class Meta:
        model = Exercise
        fields = '__all__'
        depth = 1
