from django.contrib import admin


from .models import Workout, Exercise, Reps

admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Reps)
