from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Workout, Exercise, Reps



class IndexView(generic.ListView):
    """
    Lists last five finished workouts ordered by date, Lists all exercises.
    """
    model = Workout
    template_name = 'gym/index.html'
    context_object_name = 'gym_items'
    queryset = Workout.objects.order_by('-date')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_exercises'] = Exercise.objects.all().order_by('muscle')
        #To display exercise list
        context['has_open_workout'] = Workout.objects.filter(done=False).exists()
        #To verify if workout in progress
        return context

    def num_of_workouts(self):
        return Workout.objects.filter(done=True).count()

class AllWorkouts(generic.ListView):
    """
    Lists all finished exercises
    """
    model = Workout
    template_name = 'gym/all.html'
    queryset = Workout.objects.order_by('-date')


class DetailView(LoginRequiredMixin, generic.DetailView):
    """
    Displays a detail page of the workout
    """
    model = Workout
    template_name = 'gym/detail.html'
    context_object_name = 'gym_item'



class CreateExercise(LoginRequiredMixin, generic.CreateView):
    """
    Allows users to create exercises
    """
    model = Exercise
    fields = ['exercise_name', 'muscle']
    template_name = 'gym/new_exercise.html'
    success_url = reverse_lazy('gym:index')

    def form_valid(self, form):
        gym = form.instance
        gym.usr = self.request.user 
        return super().form_valid(form)



class DeleteExercise(LoginRequiredMixin, UserPassesTestMixin,generic.DeleteView):
    """
    Allows users to delete previously created exercises
    """
    model = Exercise
    context_object_name = 'item'
    template_name = 'gym/delete.html'
    success_url = reverse_lazy('gym:index')

    def test_func(self):
        obj = self.get_object()
        return obj.usr == self.request.user


class CreateWorkout(LoginRequiredMixin, generic.CreateView):
    """
    Allows users to create a new workout
    """
    def get(request, *args, **kwargs):
        if Workout.objects.filter(done=False):
            return HttpResponseRedirect(reverse_lazy('gym:active_workout'))
        return super().get(*args, **kwargs)
    #Redirection if user tries to create a workout when one exists

    model = Workout
    fields = ['title','date']
    template_name = 'gym/create.html'
    success_url = reverse_lazy('gym:active_workout')


    def form_valid(self, form):
        gym = form.instance
        gym.usr = self.request.user 
        return super().form_valid(form)



class ActiveWorkout(LoginRequiredMixin, UserPassesTestMixin , generic.CreateView):
    """
    Allows users to add specifications about the workout
    """
    model = Reps
    fields = ['exercise','rep_count','kg']
    template_name = 'gym/active_workout.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reps'] = Reps.objects.all()
        return context

    def get_success_url(self):
        return self.request.path

    def test_func(self):
        obj = self.get_object()
        return obj.usr == self.request.user



def finish(request):
    """
    Allows users to finish a workout
    """
    if Workout.objects.get(done=False):
        Workout.objects.update(done=True)
    return HttpResponseRedirect(reverse_lazy('gym:index'))
