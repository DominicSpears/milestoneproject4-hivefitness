from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('managecategories/', views.all_categories, name='categories'),
    path('addcategory/', views.add_category, name='add_category'),
    path('editcategory/<int:category_id>/', views.edit_category, name='edit_category'),
    path('deletecategory/<int:category_id>/', views.delete_category, name='delete_category'),
]
