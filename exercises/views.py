from django.shortcuts import render,redirect
from .models import Exercise

# Create your views here.

def exercise_page(request):
    """ A view to return the index page """

    return render(request, 'exercises/exercise_page.html')


def exercises_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercises/exercises_list.html', {"exercises": exercises},)
