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



# def update_booking(request, pk):
#     """
#     view to update bookings
#     **context**
#     ``booking``
#     an instance of booking.customer
#     ``tables``
#     all approved tables related to table.approved
#     ``form``
#     related to forms BookingForm
#     *template*
#     ``booking/booking.html``
#     """
#     booking = get_object_or_404(Booking, pk=pk)
#     booking_form = BookingForm(data=request.POST or None, instance=booking)
#     if request.method == "POST":
#         booking = get_object_or_404(Booking, pk=pk)
#         if booking_form.is_valid() and booking.customer == request.user:
#             booking = booking_form.save(commit=False)
#             booking.save()
#             messages.add_message(request, messages.SUCCESS, 'Booking Updated!')
#             return redirect('home_page')
#         else:
#             messages.add_message(
#                 request, messages.ERROR, 'Error updating booking!')
#             return render(request, 'booking/booking.html', context)
#     else:
#         context = {
#             'form': booking_form
#         }
#     return render(request, 'booking/booking.html', context)


# @login_required
# def cancel_booking(request, pk):
#     """
#     view to cancel bookings
#     **context**
#     ``booking``
#     an instance of booking
#     ``form``
#     related to forms BookingForm
#     *template*
#     ``booking/cancel_booking.html``
#     """
#     booking = get_object_or_404(Booking, id=pk)
#     if booking.customer != request.user:
#         messages.add_message(
#             request, messages.ERROR, 'You do not have any bookings.')
#         return redirect('home_page')
#     if request.method == 'POST':
#         form = CancelBookingForm(request.POST, instance=booking)
#         if form.is_valid():
#             cancelled_booking = form.save(commit=False)
#             booking = get_object_or_404(Booking, id=cancelled_booking.id)
#             booking.delete()
#             messages.add_message(
#                 request, messages.SUCCESS, 'Booking cancelled')
#             return redirect('customer_bookings')
#     else:
#         form = CancelBookingForm(instance=booking)
#         context = {
#             'form': form,
#             'booking': booking
#         }

#         return render(request, 'booking/cancel_booking.html', context)
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


        
