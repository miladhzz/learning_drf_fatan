from . import views
from django.urls import path

urlpatterns = [
    path('users/', views.users),
    path('calc/', views.calc),
]
