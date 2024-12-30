from django.shortcuts import render, get_object_or_404, reverse
from .models import Exercise

# Create your views here.

def exercise_page(request):
    """ A view to return the index page """

    return render(request, 'exercises/exercise_page.html')


def glutes_exercises(request): 
    exercises = Exercise.objects.all()
    return render(request, 'exercises/glutes_exercises.html', {"exercises": exercises},)


def abs_exercises(request):
    exercises = Exercise.objects.all()
    return render (request, 'exercises/abs_exercises.html', {"exercises": exercises})


