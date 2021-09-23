from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('managecategories/', views.all_categories, name='categories'),
    #path('addpostcategory/', views.add_postcategory, name='add_postcategory'),
    #path('editpostcategory/<int:postcategory_id>/', views.edit_postcategory, name='edit_postcategory'),
    #path('deletepostcategory/<int:postcategory_id>/', views.delete_postcategory, name='delete_postcategory'),

]
