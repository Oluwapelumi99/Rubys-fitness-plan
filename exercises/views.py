# from django.shortcuts import render, get_object_or_404, reverse
# from .models import Exercise, MealPlan

# # Create your views here.

# def exercise_page(request):
#     """ A view to return the index page """

#     return render(request, 'plans/exercise_page.html')


# def glutes_exercises(request): 
#     exercises = Exercise.objects.all()
#     return render(request, 'plans/glutes_exercises.html', {"exercises": exercises},)


# def abs_exercises(request):
#     exercises = Exercise.objects.all()
#     return render (request, 'plans/abs_exercises.html', {"exercises": exercises})


# def mealplan_list(request):
#     """ A view to return the index page """

#     return render(request, 'plans/exercise_page.html')