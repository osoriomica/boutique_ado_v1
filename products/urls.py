from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'), # products
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'), # add products
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'), # edit products
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'), # delete products
]
