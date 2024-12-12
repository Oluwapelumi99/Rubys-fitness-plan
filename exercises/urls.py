from . import views
from django.urls import path

urlpatterns = [
    path('exercise_page/', views.exercise_page, name='exercise_page'),
    path('exercises_list/', views.exercises_list, name='exercises_list'),
]