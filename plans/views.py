from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Exercise, MealPlan
from .forms import MealPlanForm, ExerciseForm, DeleteExerciseForm

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




@login_required
def add_exercise(request):
    """ Add a exercise to the app """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect('home')

    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            exercise = form.save()
            messages.success(request, 'Successfully added exercise!')
            return redirect('exercise_page')
        else:
            messages.error(request, 'Failed to add exercise. Please ensure the form is valid.')
    else:
        form = ExerciseForm()
        
    template = 'plans/add_exercises.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_exercise(request, exercise_id):
    """ Edit a Exercise """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect(reverse('home'))

    exercise = get_object_or_404(Exercise, pk=exercise_id)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES, instance=exercise)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated exercises!')
            return redirect('exercise_page')
        else:
            messages.error(request, 'Failed to update. Please ensure the form is valid.')
    else:
        form = ExerciseForm(instance=exercise)
        messages.info(request, f'You are editing {exercise.name}')

    template = 'plans/edit_exercises.html'
    context = {
        'form': form,
        'exercise': exercise,
    }

    return render(request, template, context)


@login_required
def delete_exercise(request, pk):
    """ Delete an exercise from the app """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect(reverse('home'))

    exercise= get_object_or_404(Exercise, id=pk)
    if request.method == 'POST':
        form = DeleteExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            deleted_exercise = form.save(commit=False)
            exercise = get_object_or_404(Exercise, id=deleted_exercise.id)
            exercise.delete()
            messages.add_message(
                request, messages.SUCCESS, 'Exercise deleted')
            return redirect('exercise_page')
    else:
        form = DeleteExerciseForm(instance=exercise)
        context = {
            'form': form,
            'exercise': exercise
        }

        return render(request, 'plans/delete_exercises.html', context)

        
