from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users2', views.UserList)

urlpatterns = [
    path('calc/', views.calc),
    path('calc2/', views.calc_json_response),
    path('add-user/', views.add_user, name='add_user'),
    path('add-user2/', views.add_user_model, name='add_user_model'),
    path('users/', views.all_user),
]

urlpatterns += router.urls
