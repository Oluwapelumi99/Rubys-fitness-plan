from . import views
from django.urls import path

urlpatterns = [
    path('plans/exercise_page/', views.exercise_page, name='exercise_page'),
    path('glutes_exercises/', views.glutes_exercises, name='glutes_exercises'),
    path('abs_exercises/', views.abs_exercises, name='abs_exercises'),
    path('', views.MealPlanList.as_view(), name='MealPlanList'),
    path('add/', views.add_exercise, name='add_exercise'),
    path('edit/<int:exercise_id>/', views.edit_exercise, name='edit_exercise'),
    path('delete/<int:exercise_id>/', views.delete_exercise, name='delete_exercise'),
    path('<slug:slug>/', views.mealplan, name='mealplan'),
]
