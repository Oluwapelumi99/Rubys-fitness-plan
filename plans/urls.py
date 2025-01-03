from . import views
from django.urls import path

urlpatterns = [
    path('plans/exercise_page/', views.exercise_page, name='exercise_page'),
    path('glutes_exercises/', views.glutes_exercises, name='glutes_exercises'),
    path('abs_exercises/', views.abs_exercises, name='abs_exercises'),
    path('', views.MealPlanList.as_view(), name='MealPlanList'),
    path('<slug:slug>/', views.mealplan, name='mealplan'),
    #  path('<slug:slug>/plan/add_meals/',
    #      views.add_meals, name='add_meals'),
    # # path('<slug:slug>/delete_comment/<int:comment_id>',
    #      views.comment_delete, name='comment_delete'),

]