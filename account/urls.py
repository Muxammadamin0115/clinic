from django.urls import path
from .views import *

urlpatterns = [
    path('sang-up/', sang_up_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('edit-user/<int:pk>/', edit_user_view),
    path('delete-user/<int:pk>/', delete_user),
]