from django.urls import path
from .views import age_calculator_view

urlpatterns = [
    path('', age_calculator_view, name='age_calculator'),
]