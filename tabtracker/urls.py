from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from tabtrackerapi.views import login_user, register_user, LessonView, RoutineView, ExerciseView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'lessons', LessonView, 'lesson')
router.register(r'routines', RoutineView, 'routine')
router.register(r'exercises', ExerciseView, 'exercise')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))
]