from django.urls import path

from .views import *

urlpatterns = [
    path('healthcheck/', healthcheck),
    
    path('all', get_all_products),
    path('categories/all', get_all_categories),
    
    path('<int:product_id>', get_product),
    path('categories/<int:category_id>', get_category),

    path('create', create_product),
    path('category/create', create_category),

    path('transaction', make_product_transaction),
    path('report', get_report)
]