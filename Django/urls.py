from django.urls import path
from . import views

urlpatterns = [
    path('Django/', views.get_items, name='get_Django'),
    path('Django/Create/', views.create_item, name='create_Django'),
]
