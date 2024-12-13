from . import views
from django.urls import path

urlpatterns = [
    path('exercise_page/', views.exercise_page, name='exercise_page'),
    path('exercises_list/', views.exercises_list, name='exercises_list'),
    path('glutes_week1/', views.glutes_week1, name='glutes_week1'),
    path('glutes_week2/', views.glutes_week2, name='glutes_week2'),
    path('glutes_week3/', views.glutes_week3, name='glutes_week3'),
    path('glutes_week4/', views.glutes_week4, name='glutes_week4'),
]