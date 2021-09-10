from django.db import models

class Exercise(models.Model):
    """Exercise Model
    Fields:
        routine_id (Foreign Key): The id of the routine the exercise is attached to
        description (CharField): A description of what the exercise is  
    """

    routine = models.ForeignKey("Routine", on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description