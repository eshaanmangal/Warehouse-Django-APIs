from django.urls import path

from .views import CategoryViews, ProductViews, ProductTranscationViews

urlpatterns = [
    
    path('', ProductViews.as_view()),
    path('<int:id>', ProductViews.as_view()),
    
    path('category', CategoryViews.as_view()),
    path('category/<int:id>', CategoryViews.as_view()),
    
    path('transaction', ProductTranscationViews.as_view()),
    path('transaction/<int:id>', ProductTranscationViews.as_view())
]