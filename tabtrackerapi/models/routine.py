from django.db import models, router
from django.contrib.auth.models import User

class Routine(models.Model):
    """Routine Model
    Fields:
        user_id (Foreign Key): The id of the user who created the routine
        routine_name (CharField): Name of the routine
        description (CharField): A description of the routine
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    routine_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.routine_name