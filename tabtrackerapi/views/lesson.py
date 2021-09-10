"""View module for handling requests for lessons"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from tabtrackerapi.models import Lesson

class LessonView(ViewSet):
    """Tab Tracker Lessons"""
    def list(self, request, pk=None):
        """Handle GET requests for all lessons

        Returns:
            Response -- JSON serialized lesson
        """
        try:
            lessons = Lesson.objects.filter(user=request.auth.user)

            serializer = LessonSerializer(
                lessons, many=True, context={'request': request})
            
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single lessons

        Returns:
            Response -- JSON serialized lesson
        """
        try:
            lesson = Lesson.objects.get(pk=pk)
            serializer = LessonSerializer(
                lesson, many=False, context={'request': request})

            return Response(serializer.data)
        
        except Exception as ex:
            return HttpResponseServerError(ex)

class LessonSerializer(serializers.ModelSerializer):
    """JSON serializer for lessons

    Arguments:
        serializers
    """
    class Meta:
        model = Lesson
        fields = ('id', 'user', 'lesson_name', 'link', 'description')