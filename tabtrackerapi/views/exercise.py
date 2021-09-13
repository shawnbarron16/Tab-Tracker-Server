"""View module for handling requests for exercises"""
from django.http import HttpResponseServerError
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from tabtrackerapi.models import Exercise, Routine, exercise

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

    def create(self, request):
        """Handles POST requests for exercises
        Returns:
            Response -- JSON serialized exercise data

            For a create for an exercise a routine must be passed in a a
            query parameter, we get the routine id from the url and the use
            Routine.objects.get to get the routine with the matching id from
            the url and pass it in as the routine the exercise is assigned to. 
        """
        selected_routine = request.query_params.get('routine', None)      

        try:
            exercise = Exercise.objects.create(
                routine = Routine.objects.get(pk=selected_routine),
                description = request.data['description'],
            )
            serializer = ExerciseSerializer(
                exercise, many=False, context={'request': request}
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk=None):
        """Handles PUT requests for exercise
        Returns:
            Response -- Empty body with 204 status
        We get the routine the same way we do in the create function,
        except now the routine comes after we pass the exercise id
        as a url parameter as well, this being the pk argument
        """
        selected_routine = request.query_params.get('routine', None) 

        try: 
            exercise = Exercise.objects.get(pk=pk)

            exercise.routine = Routine.objects.get(pk=selected_routine)
            exercise.description = request.data['description']
            exercise.save()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for an
        ReturnsL:
            Response -- 204 status
        """

        try:
            exercise = Exercise.objects.get(pk=pk)
            exercise.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        except Exercise.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

class ExerciseSerializer(serializers.ModelSerializer):
    """JSON serializer for exercises

    Arguments:
        serializers
    """
    class Meta:
        model = Exercise
        fields = '__all__'
        depth = 1
