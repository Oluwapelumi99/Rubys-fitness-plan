from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import GlutesExercise, AbsExercise, MealPlan
from .forms import GlutesExerciseForm, AbsExerciseForm, DeleteAbsExerciseForm, DeleteGlutesExerciseForm

# Create your views here.

def exercise_page(request):
    """ A view to return the index page """

    return render(request, 'plans/exercise_page.html')


def glutes_exercises(request): 
    glutes_exercises = GlutesExercise.objects.all()
    return render(request, 'plans/glutes_exercises.html', {"glutes_exercises": glutes_exercises},)



@login_required
def add_glutes_exercise(request):
    """ Add a glute exercise to the app """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect('home')

    if request.method == 'POST':
        form = GlutesExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            glutes_exercise = form.save()
            messages.success(request, 'Successfully added exercise!')
            return redirect('exercise_page')
        else:
            messages.error(request, 'Failed to add exercise. Please ensure the form is valid.')
    else:
        form = GlutesExerciseForm()
        
    template = 'plans/add_glutes_exercises.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_glutes_exercise(request, glutes_exercise_id):
    """ Edit a Glute Exercise """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect(reverse('home'))

    glutes_exercise = get_object_or_404(GlutesExercise, pk=glutes_exercise_id)
    if request.method == 'POST':
        form = GlutesExerciseForm(request.POST, request.FILES, instance=glutes_exercise)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated exercises!')
            return redirect('exercise_page')
        else:
            messages.error(request, 'Failed to update. Please ensure the form is valid.')
    else:
        form = GlutesExerciseForm(instance=glutes_exercise)
        messages.info(request, f'You are editing {glutes_exercise.name}')

    template = 'plans/edit_glutes_exercises.html'
    context = {
        'form': form,
        'glutes_exercise': glutes_exercise,
    }

    return render(request, template, context)


@login_required
def delete_glutes_exercise(request, pk):
    """ Delete a glutes exercise from the app """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect(reverse('home'))

    glutes_exercise= get_object_or_404(GlutesExercise, id=pk)
    if request.method == 'POST':
        form = DeleteGlutesExerciseForm(request.POST, instance=glutes_exercise)
        if form.is_valid():
            deleted_exercise = form.save(commit=False)
            glutes_exercise = get_object_or_404(GlutesExercise, id=deleted_exercise.id)
            glutes_exercise.delete()
            messages.add_message(
                request, messages.SUCCESS, 'Exercise deleted')
            return redirect('exercise_page')
    else:
        form = DeleteGlutesExerciseForm(instance=glutes_exercise)
        context = {
            'form': form,
            'glutes_exercise': glutes_exercise
        }

        return render(request, 'plans/delete_glutes_exercises.html', context)

 
def abs_exercises(request):
    abs_exercises = AbsExercise.objects.all()
    return render (request, 'plans/abs_exercises.html', {"abs_exercises": abs_exercises},)       

@login_required
def add_abs_exercise(request):
    """ Add an abs exercise to the app """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect('home')

    if request.method == 'POST':
        form = AbsExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            abs_exercise = form.save()
            messages.success(request, 'Successfully added exercise!')
            return redirect('exercise_page')
        else:
            messages.error(request, 'Failed to add exercise. Please ensure the form is valid.')
    else:
        form = AbsExerciseForm()
        
    template = 'plans/add_abs_exercises.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_abs_exercise(request, abs_exercise_id):
    """ Edit an Abs Exercise """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect(reverse('home'))

    abs_exercise = get_object_or_404(AbsExercise, pk=abs_exercise_id)
    if request.method == 'POST':
        form = AbsExerciseForm(request.POST, request.FILES, instance=abs_exercise)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated exercises!')
            return redirect('exercise_page')
        else:
            messages.error(request, 'Failed to update. Please ensure the form is valid.')
    else:
        form = AbsExerciseForm(instance=abs_exercise)
        messages.info(request, f'You are editing {abs_exercise.name}')

    template = 'plans/edit_abs_exercises.html'
    context = {
        'form': form,
        'abs_exercise': abs_exercise,
    }

    return render(request, template, context)


@login_required
def delete_abs_exercise(request, pk):
    """ Delete an abs exercise from the app """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect(reverse('home'))

    abs_exercise= get_object_or_404(AbsExercise, id=pk)
    if request.method == 'POST':
        form = DeleteAbsExerciseForm(request.POST, instance=abs_exercise)
        if form.is_valid():
            deleted_exercise = form.save(commit=False)
            abs_exercise = get_object_or_404(AbsExercise, id=deleted_exercise.id)
            abs_exercise.delete()
            messages.add_message(
                request, messages.SUCCESS, 'Exercise deleted')
            return redirect('exercise_page')
    else:
        form = DeleteAbsExerciseForm(instance=abs_exercise)
        context = {
            'form': form,
            'abs_exercise': abs_exercise
        }

        return render(request, 'plans/delete_abs_exercises.html', context)


class MealPlanList(generic.ListView):
    queryset = MealPlan.objects.all()
    template_name = "plans/mealplan_list.html"


def mealplan(request, slug): 
    """ A view to return the community page """
    queryset = MealPlan.objects.all()
    meal = get_object_or_404(queryset, slug=slug)
    return render(request, 'plans/meals_guide.html',
    {'meal': meal})