from . import views
from django.urls import path

urlpatterns = [
    path('calc/', views.calc),
    path('add-user/', views.add_user, name='add_user'),
    path('add-user2/', views.add_user_model, name='add_user_model'),
    path('users/', views.all_user),
]

