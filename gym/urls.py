from django.urls import path, include
from . import views

app_name = 'gym'

urlpatterns= [
        path('', views.IndexView.as_view(), name='index'),
        path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        path('create/', views.CreateWorkout.as_view(), name='create'),
        path('active_workout/', views.ActiveWorkout.as_view(), name='active_workout'),
        path('finish/', views.finish, name='finish'),
        path('new_exercise/', views.CreateExercise.as_view(), name='new_exercise'),
        path('delete_exercise/<int:pk>', views.DeleteExercise.as_view(),name='delete_exercise'),
        path('all_workouts/', views.AllWorkouts.as_view(), name='all'),

    ]
