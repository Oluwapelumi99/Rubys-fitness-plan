from . import views
from django.urls import path
urlpatterns = [
    # path('', views.community, name='community'),
    # path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('', views.BlogList.as_view(), name='BlogList'),
    path('<slug:slug>/', views.community, name='community'),

]