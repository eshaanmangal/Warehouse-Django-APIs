from django.urls import path

from .views import healthcheck, fetch_partner, fetch_all_partners

urlpatterns = [
    path('healthcheck/', healthcheck),
    path('<int:partner_id>', fetch_partner),
    path('', fetch_all_partners)
]