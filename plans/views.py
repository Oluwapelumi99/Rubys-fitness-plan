from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import GlutesExercise, AbsExercise, MealPlan
from .forms import (
    GlutesExerciseForm, AbsExerciseForm, DeleteAbsExerciseForm,
    DeleteGlutesExerciseForm, DeleteMealPlanForm, MealPlanForm)

# Create your views here.


def exercise_page(request):
    """A view to render the exercise page
    model:`Glutes_exercise`

    **Context**
    plans/exercise_page.html
    """

    return render(request, 'plans/exercise_page.html')


def glutes_exercises(request):
    """
    view to return the glutes exercises

    model:`GlutesExercise`.

    **Context**

    **Template:**

    :template:`plans/glutes_exercises.html`
    """
    glutes_exercises = GlutesExercise.objects.all()
    return render(
        request,
        'plans/glutes_exercises.html', {"glutes_exercises": glutes_exercises},)


@login_required
def add_glutes_exercise(request):
    """
    view to add glutes exercises

    model:`GlutesExercise`.

    **Context**

    **Template:**

    :template:`plans/add_glutes_exercises.html`
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect('home')

    if request.method == 'POST':
        form = GlutesExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            glutes_exercise = form.save()
            messages.success(request, 'Successfully added exercise!')
            return redirect('glutes_exercises')
        else:
            messages.error(
                request,
                'Failed to add exercise. Please ensure the form is valid.')
    else:
        form = GlutesExerciseForm()

    template = 'plans/add_glutes_exercises.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_glutes_exercise(request, glutes_exercise_id):
    """
    view to edit glutes exercises

    model:`GlutesExercise`.

    **Context**

    **Template:**

    :template:`plans/edit_glutes_exercises.html`
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect(reverse('home'))

    glutes_exercise = get_object_or_404(GlutesExercise, pk=glutes_exercise_id)
    if request.method == 'POST':
        form = GlutesExerciseForm(
            request.POST, request.FILES, instance=glutes_exercise)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated exercises!')
            return redirect('glutes_exercises')
        else:
            messages.error(
                request, 'Failed to update. Please ensure the form is valid.')
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
    """
    view to delete glutes exercises

    model:`GlutesExercise`.

    **Context**

    **Template:**

    :template:`plans/delete_glutes_exercises.html`
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect(reverse('home'))

    glutes_exercise = get_object_or_404(GlutesExercise, id=pk)
    if request.method == 'POST':
        form = DeleteGlutesExerciseForm(request.POST, instance=glutes_exercise)
        if form.is_valid():
            deleted_exercise = form.save(commit=False)
            glutes_exercise = get_object_or_404(
                GlutesExercise, id=deleted_exercise.id)
            glutes_exercise.delete()
            messages.add_message(
                request, messages.SUCCESS, 'Exercise deleted')
            return redirect('glutes_exercises')
    else:
        form = DeleteGlutesExerciseForm(instance=glutes_exercise)
        context = {
            'form': form,
            'glutes_exercise': glutes_exercise
        }

        return render(request, 'plans/delete_glutes_exercises.html', context)


def abs_exercises(request):
    abs_exercises = AbsExercise.objects.all()
    return render(
            request, 'plans/abs_exercises.html',
            {"abs_exercises": abs_exercises},)


@login_required
def add_abs_exercise(request):
    """
    view to add abs exercises

    model:`AbsExercise`.

    **Context**

    **Template:**

    :template:`plans/add_abs_exercises.html`
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect('home')

    if request.method == 'POST':
        form = AbsExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            abs_exercise = form.save()
            messages.success(request, 'Successfully added exercise!')
            return redirect('abs_exercises')
        else:
            messages.error(
                request,
                'Failed to add exercise. Please ensure the form is valid.')
    else:
        form = AbsExerciseForm()

    template = 'plans/add_abs_exercises.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_abs_exercise(request, abs_exercise_id):
    """
    view to edit abss exercises

    model:`AbsExercise`.

    **Context**

    **Template:**

    :template:`plans/edit_abs_exercises.html`
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect(reverse('home'))

    abs_exercise = get_object_or_404(AbsExercise, pk=abs_exercise_id)
    if request.method == 'POST':
        form = AbsExerciseForm(
            request.POST, request.FILES, instance=abs_exercise)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated exercises!')
            return redirect('abs_exercises')
        else:
            messages.error(
                request, 'Failed to update. Please ensure the form is valid.')
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
    """
    view to delete glutes exercises

    model:`AbsExercise`.

    **Context**

    **Template:**

    :template:`plans/delete_abs_exercises.html`
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect(reverse('home'))

    abs_exercise = get_object_or_404(AbsExercise, id=pk)
    if request.method == 'POST':
        form = DeleteAbsExerciseForm(request.POST, instance=abs_exercise)
        if form.is_valid():
            deleted_exercise = form.save(commit=False)
            abs_exercise = get_object_or_404(
                AbsExercise, id=deleted_exercise.id)
            abs_exercise.delete()
            messages.add_message(
                request, messages.SUCCESS, 'Exercise deleted')
            return redirect('abs_exercises')
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
    """
    view to return the community page

    model:`MealPlan`.

    **Context**

    **Template:**

    :template:`plans/meals_guide.html`
    """
    queryset = MealPlan.objects.all()
    meal = get_object_or_404(queryset, slug=slug)
    return render(request, 'plans/meals_guide.html', {'meal': meal})


@login_required
def add_meals(request):
    """
    view to add meal plan

    model:`MealPlan`.

    **Context**

    **Template:**

    :template:`plans/add_meals.html`
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect('home')

    if request.method == 'POST':
        form = MealPlanForm(request.POST, request.FILES)
        if form.is_valid():
            mealplan = form.save()
            messages.success(request, 'Successfully added new mealplan!')
            return redirect('MealPlanList')
        else:
            messages.error(
                request,
                'Failed to add mealplan. Please ensure the form is valid.')
    else:
        form = MealPlanForm()
    template = 'plans/add_meals.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_meal(request, meal_id):
    """
    view to edit meal plan

    model:`MealPlan`.

    **Context**

    **Template:**

    :template:`plans/edit_meals.html`
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect(reverse('home'))

    meal = get_object_or_404(MealPlan, pk=meal_id)
    if request.method == 'POST':
        form = MealPlanForm(request.POST, request.FILES, instance=meal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated mealplan!')
            return redirect('MealPlanList')
        else:
            messages.error(
                    request,
                    'Failed to update. Please ensure the form is valid.')
    else:
        form = MealPlanForm(instance=meal)
        messages.info(request, f'You are editing {meal.name}')

    template = 'plans/edit_meals.html'
    context = {
        'form': form,
        'meal': meal,
    }

    return render(request, template, context)


@login_required
def delete_meal(request, pk):
    """
    view to delete meal plan

    model:`MealPlan`.

    **Context**

    **Template:**

    :template:`plans/delete_meals.html`
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized users can do this.')
        return redirect(reverse('home'))

    meal = get_object_or_404(MealPlan, id=pk)
    if request.method == 'POST':
        form = MealPlanForm(request.POST, instance=meal)
        if form.is_valid():
            deleted_meal = form.save(commit=False)
            meal = get_object_or_404(MealPlan, id=deleted_meal.id)
            meal.delete()
            messages.add_message(
                request, messages.SUCCESS, 'Meal deleted')
            return redirect('MealPlanList')
    else:
        form = MealPlanForm(instance=meal)
        context = {
            'form': form,
            'meal': meal
        }

        return render(request, 'plans/delete_meal.html', context)
