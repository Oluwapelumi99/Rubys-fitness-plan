from . import views
from django.urls import path

urlpatterns = [
    path('plans/exercise_page/', views.exercise_page, name='exercise_page'),
    path('glutes_exercises/', views.glutes_exercises, name='glutes_exercises'),
    path('abs_exercises/', views.abs_exercises, name='abs_exercises'),
    path('', views.MealPlanList.as_view(), name='MealPlanList'),
    path('add/glutes/', views.add_glutes_exercise, name='add_glutes_exercise'),
    path('edit_glutes/<int:glutes_exercise_id>/', views.edit_glutes_exercise, name='edit_glutes_exercise'),
    path(
        'delete_glutes_exercise/<str:pk>/',
        views.delete_glutes_exercise, name='delete_glutes_exercise'),
    path('add/abs/', views.add_abs_exercise, name='add_abs_exercise'),
    path('edit_abs<int:abs_exercise_id>/', views.edit_abs_exercise, name='edit_abs_exercise'),
    path(
        'delete_abs_exercise/<str:pk>/',
        views.delete_abs_exercise, name='delete_abs_exercise'),

    path('<slug:slug>/', views.mealplan, name='mealplan'),
    path('add/meals/', views.add_meals, name='add_meals'),
    path('edit_meal/<int:meal_id>/', views.edit_meal, name='edit_meal'),
    path(
        'delete_meal/<str:pk>/',
        views.delete_meal, name='delete_meal'),
]
