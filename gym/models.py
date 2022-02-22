from django.db import models
from django.conf import settings
from django.utils import timezone

class Workout(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now(), blank=True, null=True)
    done = models.BooleanField(default=False)
    usr = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=200)
    usr = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    MUSCLE_TYPE = (
            ('Back', 'Back'),
            ('Chest', 'Chest'),
            ('Shoulders', 'Shoulders'),
            ('Legs', 'Legs'),
            ('Bicep', 'Bicep'),
            ('Tricep', 'Tricep'),
            ('Forearm', 'Forearm'),
        )

    muscle = models.CharField(max_length=10, choices=MUSCLE_TYPE)

    def __str__(self):
        return str(self.exercise_name)



class Reps(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, null=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    rep_count = models.CharField(max_length=200)
    kg = models.DecimalField(max_digits=6, decimal_places=2)

    
