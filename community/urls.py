from . import views
from django.urls import path
urlpatterns = [
    # path('', views.community, name='community'),
    # path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('', views.BlogList.as_view(), name='BlogList'),
    path('<slug:slug>/', views.community, name='community'),
     path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),

]