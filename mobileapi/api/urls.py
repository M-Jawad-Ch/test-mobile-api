from django.urls import path
from . import views

urlpatterns = [
    path('units/<ph>/', views.get_units),
    path('visit/<ph>/', views.make_visit)
]
