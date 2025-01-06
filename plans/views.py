from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Exercise, MealPlan
from .forms import MealPlanForm, ExerciseForm

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


# def mealplan(request, slug): 
#     """ A view to return the community page """
#     queryset = MealPlan.objects.all()
#     meal = get_object_or_404(queryset, slug=slug)
#     return render(request, 'plans/meals_guide.html',
#     {'meal': meal})



@login_required
def add_exercises(request):
    """ Add a exercise to the app """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            exercise = form.save()
            messages.success(request, 'Successfully added exercise!')
            return redirect(reverse('home', args=[exercise.id]))
        else:
            messages.error(request, 'Failed to add exercise. Please ensure the form is valid.')
    else:
        form = ExerciseForm()
        
    template = 'plans/add_exercises.html'
    context = {
        'form': form,
    }

    return render(request, template, context)



# @login_required
# def add_meals(request):
#     """ Add a product to the store """
#     if not request.user.is_superuser:
#         messages.error(request, 'Sorry, only store owners can do that.')
#         return redirect(reverse('home'))
    
#     mealplan_form = MealPlanForm(request.POST)
#     queryset = MealPlan.objects.all()
#     mealplan = get_object_or_404(queryset)
#     mealplan_count = MealPlan.objects.all().count()

#     if request.method == "POST":
#         mealplan_form = MealPlanForm(data=request.POST)
#         if mealplan_form.is_valid():
#             mealplan = mealplan_form.save(commit=False)
#             mealplan.author = request.user
#             mealplan.save()
#             messages.add_message(
#         request, messages.SUCCESS,
#         'Comment submitted and awaiting approval'
#     )

#     return render(request, 'plans/add_meals.html', 
#     {
#     "mealplan": mealplan,
#     "mealplan_count": mealplan_count,
#     "mealplan_form": mealplan_form,})
#     # if request.method == 'POST':
#     #     form = MealPlanForm(request.POST, request.FILES)
#     #     if form.is_valid():
#     #         mealplan = form.save()
#     #         messages.success(request, 'Successfully added meal!')
#     #         return redirect(reverse('mealplan', args=[mealplan.id]))
#     #     else:
#     #         messages.error(request, 'Failed to add product. Please ensure the form is valid.')
#     # else:
#     #     form = MealPlanForm()
        
#     # template = 'plans/add_meals.html'
#     # context = {
#     #     'form': form,
#     # }

#     return render(request, template, context)


        
