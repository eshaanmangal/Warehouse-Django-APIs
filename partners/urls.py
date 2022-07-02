from django.urls import path

from .views import healthcheck, fetch_partner, fetch_all_partners, create_category

urlpatterns = [
    path('healthcheck', healthcheck),
    path('<int:partner_id>', fetch_partner),
    path('all', fetch_all_partners),
    path('create', create_category)
]