from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add/', views.add_post, name='add_post'),
    path('<slug:slug>/', views.post, name='post'),
    path('delete_comment/<int:comment_id>/',
         views.delete_comment,
         name='delete_comment'),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/',
         views.delete_post,
         name='delete_post'),
]
