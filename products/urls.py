from django.urls import path

from .views import healthcheck, get_category, get_all_categories, create_category

urlpatterns = [
    path('healthcheck/', healthcheck),
    path('categories/<int:category_id>', get_category),
    path('categories/', get_all_categories),
    path('category', create_category)
]