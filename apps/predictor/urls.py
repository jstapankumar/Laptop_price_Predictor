from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict, name='predict'),
    path('uniquelist/', views.unique_list, name='unique_list'),
]