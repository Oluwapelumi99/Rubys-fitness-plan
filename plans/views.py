from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Exercise, MealPlan

# Create your views here.

def exercise_page(request):
    """ A view to return the index page """

    return render(request, 'plans/exercise_page.html')


def glutes_exercises(request): 
    exercises = Exercise.objects.all()
    return render(request, 'plans/glutes_exercises.html', {"exercises": exercises},)


def abs_exercises(request):
    exercises = Exercise.objects.all()
    return render (request, 'plans/abs_exercises.html', {"exercises": exercises},)


class MealPlanList(generic.ListView):
    queryset = MealPlan.objects.all()
    template_name = "plans/mealplan_list.html"


def mealplan(request, slug): 
    """ A view to return the community page """
    queryset = MealPlan.objects.all()
    meal = get_object_or_404(queryset, slug=slug)
    return render(request, 'plans/meals_guide.html',
    {'meal': meal})
