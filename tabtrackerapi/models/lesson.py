from tabtrackerapi.models import user
from django.db import models
from django.contrib.auth.models import User

class Lesson(models.Model):
    """Lesson Model
    Fields:
        user_id (Foreign Key): Id of the user who created the lesson
        lesson_name (CharField): Name of the lesson
        link (Charfield): Link to the actual lesson
        description (Charfield): A description of the lesson
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.lesson_name