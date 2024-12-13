from django.shortcuts import render,redirect
from .models import Exercise, Abs_exercise

# Create your views here.

def exercise_page(request):
    """ A view to return the index page """

    return render(request, 'exercises/exercise_page.html')


def exercises_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercises/exercises_list.html', {"exercises": exercises},)



def Abs_exercise_list(request):
    abs_exercises = Abs_exercise.objects.all()
    return render(request, 'exercises/abs_exercises_list.html', {"abs_exercises": abs_exercises},)

