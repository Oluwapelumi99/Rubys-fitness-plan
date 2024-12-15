from django.shortcuts import render,redirect
from .models import Exercise

# Create your views here.

def exercise_page(request):
    """ A view to return the index page """

    return render(request, 'exercises/exercise_page.html')


def exercises_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercises/exercises_list.html', {"exercises": exercises},)


def glutes_week1(request):
    exercises = Exercise.objects.all()
    print("excersises = ", exercises)
    return render (request, 'exercises/glutes_week1.html', {"exercises": exercises})


def glutes_week2(request):
    exercises = Exercise.objects.all()
    return render (request, 'exercises/glutes_week2.html', {"exercises": exercises})


def glutes_week3(request):
    exercises = Exercise.objects.all()
    return render (request, 'exercises/glutes_week3.html', {"exercises": exercises})


def glutes_week4(request):
    exercises = Exercise.objects.all()
    return render (request, 'exercises/glutes_week4.html', {"exercises": exercises})