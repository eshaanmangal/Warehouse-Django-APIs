from django.urls import path

from .views import healthcheck, get_category, get_product, get_all_categories, get_all_products, create_category, create_product

urlpatterns = [
    path('healthcheck/', healthcheck),
    
    path('all', get_all_products),
    path('categories/all', get_all_categories),
    
    path('<int:product_id>', get_product),
    path('categories/<int:category_id>', get_category),

    path('create', create_product),
    path('category/create', create_category)
]