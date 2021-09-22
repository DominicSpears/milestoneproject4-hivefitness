from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='posts'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('managecategories/', views.all_postcategories, name='postcategories'),
    path('addpostcategory/', views.add_postcategory, name='add_postcategory'),
]
